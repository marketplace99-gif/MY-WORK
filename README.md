# Library Management System

A comprehensive Python library management system that allows you to manage books, members, borrowing, and returning operations.

## Features

- **Book Management**: Add, remove, and search books by title, author, or ISBN
- **Member Management**: Register and manage library members
- **Borrowing & Returning**: Borrow and return books with transaction tracking
- **Search Functionality**: Search books by title, author, or ISBN
- **Statistics**: View detailed library statistics and availability
- **Transaction History**: Track all borrowing and returning transactions

## Project Structure

```
library_system/
├── book.py          # Book class definition
├── member.py        # Member class definition
└── library.py       # Main Library class with all operations
example_usage.py    # Example usage demonstration
```

## Classes

### Book
Represents a book in the library.

**Attributes:**
- `title`: Book title
- `author`: Book author
- `isbn`: ISBN number
- `publication_year`: Year published
- `total_copies`: Total copies in library
- `available_copies`: Currently available copies

**Methods:**
- `borrow_book()`: Borrow a copy
- `return_book()`: Return a copy
- `is_available()`: Check if available

### Member
Represents a library member.

**Attributes:**
- `name`: Member name
- `email`: Email address
- `member_id`: Unique member ID
- `borrowed_books`: List of borrowed books
- `join_date`: Registration date
- `is_active`: Member status

**Methods:**
- `add_borrowed_book()`: Record borrowed book
- `remove_borrowed_book()`: Record returned book
- `get_borrowed_books_count()`: Count borrowed books

### Library
Main library management system.

**Key Methods:**
- `add_book()`: Add a new book
- `remove_book()`: Remove a book
- `register_member()`: Register a new member
- `search_book_by_title()`: Search by title
- `search_book_by_author()`: Search by author
- `search_book_by_isbn()`: Search by ISBN
- `borrow_book()`: Borrow a book for a member
- `return_book()`: Return a borrowed book
- `get_available_books()`: List available books
- `get_library_statistics()`: Get library stats

## Usage

Run the example:
```bash
python example_usage.py
```

### Basic Example

```python
from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

# Create library
library = Library("My Library")

# Add a book
book = Book(
    title="Python Programming",
    author="John Doe",
    isbn="123-456-789",
    publication_year=2023,
    total_copies=5
)
library.add_book(book)

# Register a member
member = Member("Alice", "alice@example.com", "M001")
library.register_member(member)

# Borrow a book
library.borrow_book("M001", "123-456-789")

# Return a book
library.return_book("M001", "123-456-789")

# View statistics
library.display_statistics()
```

## Requirements

Python 3.6+

No external dependencies required!

## License

MIT License
