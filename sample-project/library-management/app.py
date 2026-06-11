from __future__ import annotations

import os
from functools import wraps
from datetime import datetime, timedelta

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import or_

from extensions import db, login_manager
from models import Book, BorrowRequest, Category, Loan, User


def role_required(*roles: str):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)
            return view(*args, **kwargs)

        return wrapped

    return decorator


def seed_demo_data() -> None:
    if Category.query.first() is not None:
        return

    fiction = Category(name="Fiction")
    history = Category(name="History")
    science = Category(name="Science")
    db.session.add_all([fiction, history, science])
    db.session.flush()

    books = [
        Book(
            title="Clean Code",
            author="Robert C. Martin",
            isbn="9780132350884",
            summary="Practical guidance for writing readable, maintainable software.",
            total_copies=3,
            available_copies=2,
            category=science,
        ),
        Book(
            title="Sapiens",
            author="Yuval Noah Harari",
            isbn="9780062316097",
            summary="A broad history of humankind and the forces that shaped society.",
            total_copies=2,
            available_copies=0,
            category=history,
        ),
        Book(
            title="The Pragmatic Programmer",
            author="Andrew Hunt and David Thomas",
            isbn="9780201616224",
            summary="Core practices for thoughtful, adaptable software development.",
            total_copies=4,
            available_copies=4,
            category=science,
        ),
    ]
    librarian = User(
        email="librarian@university.edu",
        full_name="Campus Librarian",
        role="librarian",
    )
    librarian.set_password("librarian123")
    db.session.add(librarian)
    db.session.add_all(books)
    db.session.commit()


def role_home(user: User) -> str:
    if user.role == "librarian":
        return url_for("librarian_dashboard")
    return url_for("catalog")


def get_catalog_context(book: Book) -> dict:
    context = {}
    if current_user.is_authenticated and current_user.role == "student":
        context["pending_request"] = BorrowRequest.query.filter_by(
            user_id=current_user.id,
            book_id=book.id,
            status="pending",
        ).first()
        context["active_loan"] = Loan.query.filter_by(
            user_id=current_user.id,
            book_id=book.id,
            returned_at=None,
        ).first()
    return context


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="development-key",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'library.db')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        TESTING=False,
    )

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.unauthorized_handler
    def _unauthorized():
        flash("Please log in to continue.", "warning")
        return redirect(url_for("login"))

    @app.errorhandler(403)
    def forbidden(_error):
        return render_template("403.html"), 403

    with app.app_context():
        db.create_all()
        seed_demo_data()

    register_routes(app)
    return app


def register_routes(app: Flask) -> None:
    @app.route("/")
    def home():
        if current_user.is_authenticated:
            return redirect(role_home(current_user))
        return render_template("home.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(role_home(current_user))

        if request.method == "POST":
            full_name = request.form.get("full_name", "").strip()
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            if not full_name or not email or not password:
                flash("All registration fields are required.", "danger")
            elif User.query.filter_by(email=email).first():
                flash("That email is already registered.", "danger")
            elif len(password) < 8:
                flash("Password must be at least 8 characters long.", "danger")
            else:
                user = User(email=email, full_name=full_name, role="student")
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash("Registration successful. Welcome.", "success")
                return redirect(role_home(user))

        return render_template("auth/register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(role_home(current_user))

        if request.method == "POST":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")
            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user)
                flash("Logged in successfully.", "success")
                return redirect(role_home(user))

            flash("Invalid email or password.", "danger")

        return render_template("auth/login.html")

    @app.post("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.", "info")
        return redirect(url_for("home"))

    @app.route("/catalog")
    @role_required("student", "librarian")
    def catalog():
        query = Book.query.join(Category)
        search = request.args.get("q", "").strip()
        category_name = request.args.get("category", "").strip()
        availability = request.args.get("availability", "all").strip().lower()

        if search:
            like = f"%{search}%"
            query = query.filter(
                or_(
                    Book.title.ilike(like),
                    Book.author.ilike(like),
                    Book.isbn.ilike(like),
                )
            )

        if category_name:
            query = query.filter(Category.name == category_name)

        if availability == "available":
            query = query.filter(Book.available_copies > 0)
        elif availability == "unavailable":
            query = query.filter(Book.available_copies <= 0)

        books = query.order_by(Book.title.asc()).all()
        categories = Category.query.order_by(Category.name.asc()).all()

        return render_template(
            "catalog/list.html",
            books=books,
            categories=categories,
            can_manage=current_user.role == "librarian",
            filters={
                "q": search,
                "category": category_name,
                "availability": availability,
            },
        )

    @app.route("/catalog/<int:book_id>")
    @role_required("student", "librarian")
    def catalog_detail(book_id: int):
        book = db.session.get(Book, book_id)
        if book is None:
            abort(404)
        return render_template("catalog/detail.html", book=book, **get_catalog_context(book))

    @app.post("/catalog/<int:book_id>/request")
    @role_required("student")
    def request_book(book_id: int):
        book = db.session.get(Book, book_id)
        if book is None:
            abort(404)

        existing_pending = BorrowRequest.query.filter_by(
            user_id=current_user.id,
            book_id=book.id,
            status="pending",
        ).first()
        existing_loan = Loan.query.filter_by(
            user_id=current_user.id,
            book_id=book.id,
            returned_at=None,
        ).first()

        if existing_pending:
            flash("You already have a pending request for this book.", "warning")
        elif existing_loan:
            flash("You already have an active loan for this book.", "warning")
        elif not book.is_available:
            flash("This book is not available right now.", "warning")
        else:
            borrow_request = BorrowRequest(user_id=current_user.id, book_id=book.id)
            db.session.add(borrow_request)
            db.session.commit()
            flash("Borrow request submitted.", "success")

        return redirect(url_for("catalog_detail", book_id=book.id))

    @app.route("/my-borrowings")
    @role_required("student")
    def my_borrowings():
        requests = (
            BorrowRequest.query.filter_by(user_id=current_user.id)
            .order_by(BorrowRequest.requested_at.desc())
            .all()
        )
        loans = (
            Loan.query.filter_by(user_id=current_user.id)
            .order_by(Loan.borrowed_at.desc())
            .all()
        )
        return render_template("student/dashboard.html", requests=requests, loans=loans)

    @app.post("/librarian/requests/<int:request_id>/approve")
    @role_required("librarian")
    def approve_request(request_id: int):
        borrow_request = db.session.get(BorrowRequest, request_id)
        if borrow_request is None:
            abort(404)
        if borrow_request.status != "pending":
            flash("That request has already been processed.", "warning")
            return redirect(url_for("librarian_dashboard"))
        if not borrow_request.book.is_available:
            flash("The requested book is no longer available.", "warning")
            return redirect(url_for("librarian_dashboard"))

        borrow_request.status = "approved"
        borrow_request.decided_at = datetime.now()
        loan = Loan(
            user_id=borrow_request.user_id,
            book_id=borrow_request.book_id,
            request=borrow_request,
            due_date=datetime.now() + timedelta(days=14),
        )
        borrow_request.book.available_copies -= 1
        db.session.add(loan)
        db.session.commit()
        flash("Borrow request approved and loan created.", "success")
        return redirect(url_for("librarian_dashboard"))

    @app.post("/librarian/requests/<int:request_id>/reject")
    @role_required("librarian")
    def reject_request(request_id: int):
        borrow_request = db.session.get(BorrowRequest, request_id)
        if borrow_request is None:
            abort(404)
        if borrow_request.status != "pending":
            flash("That request has already been processed.", "warning")
        else:
            borrow_request.status = "rejected"
            borrow_request.decided_at = datetime.now()
            db.session.commit()
            flash("Borrow request rejected.", "info")
        return redirect(url_for("librarian_dashboard"))

    @app.post("/librarian/loans/<int:loan_id>/return")
    @role_required("librarian")
    def return_loan(loan_id: int):
        loan = db.session.get(Loan, loan_id)
        if loan is None:
            abort(404)
        if loan.returned_at is None:
            loan.returned_at = datetime.now()
            loan.book.available_copies = min(
                loan.book.total_copies, loan.book.available_copies + 1
            )
            db.session.commit()
            flash("Return recorded.", "success")
        else:
            flash("That loan has already been returned.", "warning")
        return redirect(url_for("librarian_dashboard"))

    @app.route("/librarian/books/new", methods=["GET", "POST"])
    @role_required("librarian")
    def librarian_book_create():
        categories = Category.query.order_by(Category.name.asc()).all()

        if request.method == "POST":
            title = request.form.get("title", "").strip()
            author = request.form.get("author", "").strip()
            isbn = request.form.get("isbn", "").strip()
            summary = request.form.get("summary", "").strip()
            category_id = request.form.get("category_id", "").strip()
            total_copies_raw = request.form.get("total_copies", "1").strip()
            available_copies_raw = request.form.get("available_copies", total_copies_raw).strip()

            category = db.session.get(Category, int(category_id)) if category_id.isdigit() else None

            try:
                total_copies = int(total_copies_raw)
                available_copies = int(available_copies_raw)
            except ValueError:
                total_copies = available_copies = -1

            if not title or not author or not isbn or not summary or category is None:
                flash("All book fields are required.", "danger")
            elif total_copies <= 0:
                flash("Total copies must be at least 1.", "danger")
            elif available_copies < 0 or available_copies > total_copies:
                flash("Available copies must be between 0 and total copies.", "danger")
            elif Book.query.filter_by(isbn=isbn).first():
                flash("A book with that ISBN already exists.", "danger")
            else:
                book = Book(
                    title=title,
                    author=author,
                    isbn=isbn,
                    summary=summary,
                    category=category,
                    total_copies=total_copies,
                    available_copies=available_copies,
                )
                db.session.add(book)
                db.session.commit()
                flash("Book added to the catalog.", "success")
                return redirect(url_for("librarian_dashboard"))

        return render_template(
            "librarian/book_form.html",
            categories=categories,
            form_title="Add book to catalog",
            submit_label="Save book",
            book=None,
            form_action=url_for("librarian_book_create"),
        )

    @app.route("/librarian/books/<int:book_id>/edit", methods=["GET", "POST"])
    @role_required("librarian")
    def librarian_book_edit(book_id: int):
        book = db.session.get(Book, book_id)
        if book is None:
            abort(404)

        categories = Category.query.order_by(Category.name.asc()).all()
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            author = request.form.get("author", "").strip()
            isbn = request.form.get("isbn", "").strip()
            summary = request.form.get("summary", "").strip()
            category_id = request.form.get("category_id", "").strip()
            total_copies_raw = request.form.get("total_copies", "1").strip()
            available_copies_raw = request.form.get("available_copies", total_copies_raw).strip()

            category = db.session.get(Category, int(category_id)) if category_id.isdigit() else None

            try:
                total_copies = int(total_copies_raw)
                available_copies = int(available_copies_raw)
            except ValueError:
                total_copies = available_copies = -1

            if not title or not author or not isbn or not summary or category is None:
                flash("All book fields are required.", "danger")
            elif total_copies <= 0:
                flash("Total copies must be at least 1.", "danger")
            elif available_copies < 0 or available_copies > total_copies:
                flash("Available copies must be between 0 and total copies.", "danger")
            else:
                duplicate = Book.query.filter(Book.isbn == isbn, Book.id != book.id).first()
                if duplicate:
                    flash("A book with that ISBN already exists.", "danger")
                else:
                    book.title = title
                    book.author = author
                    book.isbn = isbn
                    book.summary = summary
                    book.category = category
                    book.total_copies = total_copies
                    book.available_copies = available_copies
                    db.session.commit()
                    flash("Book updated.", "success")
                    return redirect(url_for("catalog_detail", book_id=book.id))

        return render_template(
            "librarian/book_form.html",
            categories=categories,
            form_title="Edit book",
            submit_label="Update book",
            book=book,
            form_action=url_for("librarian_book_edit", book_id=book.id),
        )

    @app.post("/librarian/books/<int:book_id>/delete")
    @role_required("librarian")
    def librarian_book_delete(book_id: int):
        book = db.session.get(Book, book_id)
        if book is None:
            abort(404)
        if book.borrow_requests or book.loans:
            flash("This book cannot be deleted while it has borrowing history.", "warning")
            return redirect(url_for("librarian_dashboard"))

        db.session.delete(book)
        db.session.commit()
        flash("Book deleted.", "info")
        return redirect(url_for("librarian_dashboard"))

    @app.route("/dashboard")
    @role_required("student", "librarian")
    def student_dashboard():
        requests = (
            BorrowRequest.query.filter_by(user_id=current_user.id)
            .order_by(BorrowRequest.requested_at.desc())
            .all()
        )
        loans = (
            Loan.query.filter_by(user_id=current_user.id)
            .order_by(Loan.borrowed_at.desc())
            .all()
        )
        return render_template("student/dashboard.html", requests=requests, loans=loans)

    @app.route("/librarian")
    @role_required("librarian")
    def librarian_dashboard():
        books = Book.query.order_by(Book.id.desc()).all()
        pending_requests = (
            BorrowRequest.query.filter_by(status="pending")
            .order_by(BorrowRequest.requested_at.asc())
            .all()
        )
        active_loans = (
            Loan.query.filter_by(returned_at=None).order_by(Loan.borrowed_at.asc()).all()
        )
        overdue_loans = [loan for loan in active_loans if loan.is_overdue]
        total_books = len(books)
        available_books = sum(1 for book in books if book.is_available)
        return render_template(
            "dashboard.html",
            books=books[:6],
            total_books=total_books,
            available_books=available_books,
            pending_requests=pending_requests,
            active_loans=active_loans,
            overdue_loans=overdue_loans,
        )


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
