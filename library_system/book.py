"""Book module for library management system."""

from datetime import datetime
from typing import Optional


class Book:
    """Represents a book in the library."""

    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
        publication_year: int,
        total_copies: int = 1,
    ):
        """Initialize a Book instance.

        Args:
            title: The title of the book
            author: The author of the book
            isbn: ISBN number of the book
            publication_year: Year the book was published
            total_copies: Total number of copies available
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.created_at = datetime.now()

    def borrow_book(self) -> bool:
        """Borrow a book if available.

        Returns:
            True if book was borrowed successfully, False otherwise
        """
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self) -> bool:
        """Return a borrowed book.

        Returns:
            True if book was returned successfully, False otherwise
        """
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def is_available(self) -> bool:
        """Check if book is available for borrowing.

        Returns:
            True if at least one copy is available
        """
        return self.available_copies > 0

    def __str__(self) -> str:
        """Return string representation of the book."""
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Publication Year: {self.publication_year}\n"
            f"Available Copies: {self.available_copies}/{self.total_copies}"
        )

    def __repr__(self) -> str:
        """Return representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
