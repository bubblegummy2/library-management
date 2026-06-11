from __future__ import annotations

from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="student")
    password_hash = db.Column(db.String(255), nullable=False)
    borrow_requests = db.relationship(
        "BorrowRequest", back_populates="user", cascade="all, delete-orphan"
    )
    loans = db.relationship("Loan", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def is_librarian(self) -> bool:
        return self.role == "librarian"

    @property
    def is_student(self) -> bool:
        return self.role == "student"


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    return db.session.get(User, int(user_id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship("Book", back_populates="category", lazy="select")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    author = db.Column(db.String(255), nullable=False, index=True)
    isbn = db.Column(db.String(32), unique=True, nullable=False, index=True)
    summary = db.Column(db.Text, nullable=False)
    total_copies = db.Column(db.Integer, nullable=False, default=1)
    available_copies = db.Column(db.Integer, nullable=False, default=1)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="books")
    borrow_requests = db.relationship(
        "BorrowRequest", back_populates="book", cascade="all, delete-orphan"
    )
    loans = db.relationship("Loan", back_populates="book", cascade="all, delete-orphan")

    @property
    def is_available(self) -> bool:
        return self.available_copies > 0

    @property
    def availability_label(self) -> str:
        return "Available" if self.is_available else "Unavailable"


class BorrowRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False, index=True)
    status = db.Column(db.String(20), nullable=False, default="pending", index=True)
    requested_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    decided_at = db.Column(db.DateTime, nullable=True)
    user = db.relationship("User", back_populates="borrow_requests")
    book = db.relationship("Book", back_populates="borrow_requests")
    loan = db.relationship("Loan", back_populates="request", uselist=False)

    @property
    def is_pending(self) -> bool:
        return self.status == "pending"


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False, index=True)
    request_id = db.Column(
        db.Integer, db.ForeignKey("borrow_request.id"), nullable=True, unique=True
    )
    borrowed_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    due_date = db.Column(db.DateTime, nullable=False)
    returned_at = db.Column(db.DateTime, nullable=True)
    user = db.relationship("User", back_populates="loans")
    book = db.relationship("Book", back_populates="loans")
    request = db.relationship("BorrowRequest", back_populates="loan")

    @property
    def is_active(self) -> bool:
        return self.returned_at is None

    @property
    def is_overdue(self) -> bool:
        return self.returned_at is None and self.due_date < datetime.now()
