"""Member module for library management system."""

from datetime import datetime
from typing import List, Optional


class Member:
    """Represents a member of the library."""

    def __init__(self, name: str, email: str, member_id: str):
        """Initialize a Member instance.

        Args:
            name: Name of the member
            email: Email address of the member
            member_id: Unique identifier for the member
        """
        self.name = name
        self.email = email
        self.member_id = member_id
        self.borrowed_books: List[dict] = []
        self.join_date = datetime.now()
        self.is_active = True

    def add_borrowed_book(self, book_title: str, isbn: str) -> None:
        """Add a borrowed book to member's record.

        Args:
            book_title: Title of the borrowed book
            isbn: ISBN of the borrowed book
        """
        self.borrowed_books.append(
            {"title": book_title, "isbn": isbn, "borrowed_date": datetime.now()}
        )

    def remove_borrowed_book(self, isbn: str) -> bool:
        """Remove a returned book from member's record.

        Args:
            isbn: ISBN of the book being returned

        Returns:
            True if book was removed, False if not found
        """
        for book in self.borrowed_books:
            if book["isbn"] == isbn:
                self.borrowed_books.remove(book)
                return True
        return False

    def get_borrowed_books_count(self) -> int:
        """Get the number of borrowed books.

        Returns:
            Number of books currently borrowed
        """
        return len(self.borrowed_books)

    def __str__(self) -> str:
        """Return string representation of the member."""
        return (
            f"Member ID: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Borrowed Books: {self.get_borrowed_books_count()}\n"
            f"Status: {'Active' if self.is_active else 'Inactive'}"
        )

    def __repr__(self) -> str:
        """Return representation of the member."""
        return f"Member(name='{self.name}', member_id='{self.member_id}')"
