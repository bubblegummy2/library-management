import tempfile
import unittest
from datetime import datetime, timedelta

from app import create_app
from extensions import db
from models import Book, BorrowRequest, Category, Loan, User


class PhaseOneWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.app = create_app(
            {
                "TESTING": True,
                "SQLALCHEMY_DATABASE_URI": f"sqlite:///{self.temp_db.name}",
                "WTF_CSRF_ENABLED": False,
                "SECRET_KEY": "test-key",
            }
        )
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def login(self, email: str, password: str):
        return self.client.post(
            "/login",
            data={"email": email, "password": password},
            follow_redirects=True,
        )

    def test_student_registration_and_catalog_access(self):
        response = self.client.post(
            "/register",
            data={
                "full_name": "Ayu Pratama",
                "email": "ayu@student.edu",
                "password": "password123",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Browse and filter books", response.data)
        self.assertIn(b"Clean Code", response.data)

        with self.app.app_context():
            user = User.query.filter_by(email="ayu@student.edu").first()
            self.assertIsNotNone(user)
            self.assertTrue(user.is_student)

    def test_catalog_search_and_filter(self):
        self.login("librarian@university.edu", "librarian123")
        self.client.post("/logout", follow_redirects=True)
        self.client.post(
            "/register",
            data={
                "full_name": "Bima",
                "email": "bima@student.edu",
                "password": "password123",
            },
            follow_redirects=True,
        )

        response = self.client.get(
            "/catalog?q=Clean&availability=available", follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Clean Code", response.data)
        self.assertNotIn(b"Sapiens", response.data)

    def test_librarian_cannot_access_student_catalog(self):
        response = self.login("librarian@university.edu", "librarian123")
        self.assertIn(b"Logged in successfully.", response.data)

        response = self.client.get("/catalog")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add new book", response.data)

    def test_librarian_can_add_book(self):
        self.login("librarian@university.edu", "librarian123")

        with self.app.app_context():
            category = Category.query.filter_by(name="Fiction").first()
            self.assertIsNotNone(category)

        response = self.client.post(
            "/librarian/books/new",
            data={
                "title": "Dune",
                "author": "Frank Herbert",
                "isbn": "9780441013593",
                "category_id": str(category.id),
                "summary": "A science fiction classic about politics, ecology, and power.",
                "total_copies": "2",
                "available_copies": "2",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Dune", response.data)
        self.assertIn(b"Book added to the catalog.", response.data)
        self.assertIn(b"Latest books in the catalog", response.data)

        with self.app.app_context():
            created = Book.query.filter_by(isbn="9780441013593").first()
            self.assertIsNotNone(created)
            self.assertEqual(created.title, "Dune")

    def test_student_can_request_book(self):
        self.client.post(
            "/register",
            data={
                "full_name": "Dina",
                "email": "dina@student.edu",
                "password": "password123",
            },
            follow_redirects=True,
        )

        with self.app.app_context():
            book = Book.query.filter_by(isbn="9780132350884").first()
            self.assertIsNotNone(book)

        response = self.client.post(
            f"/catalog/{book.id}/request",
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Borrow request submitted.", response.data)

        with self.app.app_context():
            borrow_request = BorrowRequest.query.filter_by(
                user_id=User.query.filter_by(email="dina@student.edu").first().id,
                book_id=book.id,
            ).first()
            self.assertIsNotNone(borrow_request)
            self.assertEqual(borrow_request.status, "pending")

    def test_librarian_can_approve_and_return_book(self):
        self.client.post(
            "/register",
            data={
                "full_name": "Eka",
                "email": "eka@student.edu",
                "password": "password123",
            },
            follow_redirects=True,
        )

        with self.app.app_context():
            book = Book.query.filter_by(isbn="9780132350884").first()
            self.assertIsNotNone(book)

        self.client.post(f"/catalog/{book.id}/request", follow_redirects=True)
        self.client.post("/logout", follow_redirects=True)
        self.login("librarian@university.edu", "librarian123")

        with self.app.app_context():
            borrow_request = BorrowRequest.query.filter_by(book_id=book.id).first()
            self.assertIsNotNone(borrow_request)
            starting_available = book.available_copies

        response = self.client.post(
            f"/librarian/requests/{borrow_request.id}/approve",
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Borrow request approved and loan created.", response.data)

        with self.app.app_context():
            approved_loan = Loan.query.filter_by(request_id=borrow_request.id).first()
            self.assertIsNotNone(approved_loan)
            self.assertIsNone(approved_loan.returned_at)
            updated_book = db.session.get(Book, book.id)
            self.assertEqual(updated_book.available_copies, starting_available - 1)

        response = self.client.post(
            f"/librarian/loans/{approved_loan.id}/return",
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Return recorded.", response.data)

        with self.app.app_context():
            returned_loan = db.session.get(Loan, approved_loan.id)
            self.assertIsNotNone(returned_loan.returned_at)
            updated_book = db.session.get(Book, book.id)
            self.assertEqual(updated_book.available_copies, starting_available)

    def test_librarian_dashboard_shows_overdue_loans(self):
        self.login("librarian@university.edu", "librarian123")

        with self.app.app_context():
            student = User.query.filter_by(email="student1@example.com").first()
            if student is None:
                student = User(email="student1@example.com", full_name="Student One", role="student")
                student.set_password("password123")
                db.session.add(student)
                db.session.flush()
            book = Book.query.filter_by(isbn="9780132350884").first()
            loan = Loan(
                user_id=student.id,
                book_id=book.id,
                due_date=datetime.now() - timedelta(days=1),
            )
            db.session.add(loan)
            db.session.commit()

        response = self.client.get("/librarian")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Overdue loans", response.data)
        self.assertIn(b"Overdue", response.data)

    def test_librarian_can_edit_and_delete_book(self):
        self.login("librarian@university.edu", "librarian123")

        with self.app.app_context():
            category = Category.query.filter_by(name="Fiction").first()
            self.assertIsNotNone(category)

        self.client.post(
            "/librarian/books/new",
            data={
                "title": "Foundation",
                "author": "Isaac Asimov",
                "isbn": "9780553293357",
                "category_id": str(category.id),
                "summary": "A science fiction classic.",
                "total_copies": "1",
                "available_copies": "1",
            },
            follow_redirects=True,
        )

        with self.app.app_context():
            created = Book.query.filter_by(isbn="9780553293357").first()
            self.assertIsNotNone(created)

        response = self.client.post(
            f"/librarian/books/{created.id}/edit",
            data={
                "title": "Foundation (Edited)",
                "author": "Isaac Asimov",
                "isbn": "9780553293357",
                "category_id": str(category.id),
                "summary": "An edited science fiction classic.",
                "total_copies": "2",
                "available_copies": "2",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book updated.", response.data)
        self.assertIn(b"Foundation (Edited)", response.data)

        response = self.client.post(
            f"/librarian/books/{created.id}/delete",
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book deleted.", response.data)

        with self.app.app_context():
            deleted = Book.query.filter_by(isbn="9780553293357").first()
            self.assertIsNone(deleted)

    def test_book_detail_page_shows_availability(self):
        self.client.post(
            "/register",
            data={
                "full_name": "Citra",
                "email": "citra@student.edu",
                "password": "password123",
            },
            follow_redirects=True,
        )

        with self.app.app_context():
            book = Book.query.filter_by(isbn="9780132350884").first()
            self.assertIsNotNone(book)

        response = self.client.get(f"/catalog/{book.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Availability", response.data)


if __name__ == "__main__":
    unittest.main()
