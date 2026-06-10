"""Library management system."""

from typing import List, Optional, Dict
from library_system.book import Book
from library_system.member import Member


class Library:
    """Main library management system class."""

    def __init__(self, name: str):
        """Initialize the Library.

        Args:
            name: Name of the library
        """
        self.name = name
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.transaction_history: List[dict] = []

    def add_book(self, book: Book) -> bool:
        """Add a new book to the library.

        Args:
            book: Book object to add

        Returns:
            True if book was added, False if ISBN already exists
        """
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists in library.")
            return False
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")
        return True

    def remove_book(self, isbn: str) -> bool:
        """Remove a book from the library.

        Args:
            isbn: ISBN of the book to remove

        Returns:
            True if book was removed, False if not found
        """
        if isbn in self.books:
            book = self.books.pop(isbn)
            print(f"Book '{book.title}' removed successfully.")
            return True
        print(f"Book with ISBN {isbn} not found.")
        return False

    def register_member(self, member: Member) -> bool:
        """Register a new member.

        Args:
            member: Member object to register

        Returns:
            True if member was registered, False if ID already exists
        """
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists.")
            return False
        self.members[member.member_id] = member
        print(f"Member '{member.name}' registered successfully.")
        return True

    def search_book_by_title(self, title: str) -> List[Book]:
        """Search for books by title.

        Args:
            title: Title to search for

        Returns:
            List of books matching the title
        """
        return [
            book for book in self.books.values() if title.lower() in book.title.lower()
        ]

    def search_book_by_author(self, author: str) -> List[Book]:
        """Search for books by author.

        Args:
            author: Author name to search for

        Returns:
            List of books by the author
        """
        return [
            book
            for book in self.books.values()
            if author.lower() in book.author.lower()
        ]

    def search_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Search for a book by ISBN.

        Args:
            isbn: ISBN to search for

        Returns:
            Book object if found, None otherwise
        """
        return self.books.get(isbn)

    def borrow_book(self, member_id: str, isbn: str) -> bool:
        """Borrow a book for a member.

        Args:
            member_id: ID of the member borrowing
            isbn: ISBN of the book to borrow

        Returns:
            True if book was borrowed successfully
        """
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False

        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if book.borrow_book():
            member.add_borrowed_book(book.title, isbn)
            self.transaction_history.append(
                {
                    "type": "borrow",
                    "member_id": member_id,
                    "book_title": book.title,
                    "isbn": isbn,
                }
            )
            print(
                f"Member '{member.name}' borrowed '{book.title}' successfully."
            )
            return True

        print(f"Book '{book.title}' is not available for borrowing.")
        return False

    def return_book(self, member_id: str, isbn: str) -> bool:
        """Return a borrowed book.

        Args:
            member_id: ID of the member returning
            isbn: ISBN of the book to return

        Returns:
            True if book was returned successfully
        """
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False

        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if member.remove_borrowed_book(isbn):
            book.return_book()
            self.transaction_history.append(
                {"type": "return", "member_id": member_id, "book_title": book.title}
            )
            print(f"Member '{member.name}' returned '{book.title}' successfully.")
            return True

        print(f"Member '{member.name}' doesn't have this book.")
        return False

    def get_available_books(self) -> List[Book]:
        """Get list of all available books.

        Returns:
            List of available books
        """
        return [book for book in self.books.values() if book.is_available()]

    def get_member_borrowed_books(self, member_id: str) -> Optional[List[dict]]:
        """Get books borrowed by a member.

        Args:
            member_id: ID of the member

        Returns:
            List of borrowed books or None if member not found
        """
        if member_id not in self.members:
            return None
        return self.members[member_id].borrowed_books

    def get_library_statistics(self) -> Dict:
        """Get library statistics.

        Returns:
            Dictionary with library statistics
        """
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books

        return {
            "library_name": self.name,
            "total_unique_titles": len(self.books),
            "total_copies": total_books,
            "available_copies": available_books,
            "borrowed_copies": borrowed_books,
            "total_members": len(self.members),
            "active_members": sum(
                1 for m in self.members.values() if m.is_active
            ),
        }

    def display_statistics(self) -> None:
        """Display library statistics."""
        stats = self.get_library_statistics()
        print(f"\n{'='*40}")
        print(f"Library: {stats['library_name']}")
        print(f"{'='*40}")
        print(f"Total Unique Titles: {stats['total_unique_titles']}")
        print(f"Total Copies: {stats['total_copies']}")
        print(f"Available Copies: {stats['available_copies']}")
        print(f"Borrowed Copies: {stats['borrowed_copies']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Active Members: {stats['active_members']}")
        print(f"{'='*40}\n")
