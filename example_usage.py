"""Example usage of the library management system."""

from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


def main():
    """Run example library operations."""
    # Create a library
    library = Library("Central City Library")

    # Add some books
    print("\n--- Adding Books ---")
    book1 = Book(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        isbn="978-0-06-112008-4",
        publication_year=1960,
        total_copies=5,
    )
    book2 = Book(
        title="1984",
        author="George Orwell",
        isbn="978-0-451-52493-2",
        publication_year=1949,
        total_copies=3,
    )
    book3 = Book(
        title="Pride and Prejudice",
        author="Jane Austen",
        isbn="978-0-14-143951-8",
        publication_year=1813,
        total_copies=4,
    )
    book4 = Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        isbn="978-0-7432-7356-5",
        publication_year=1925,
        total_copies=2,
    )

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Register members
    print("\n--- Registering Members ---")
    member1 = Member(name="Alice Johnson", email="alice@example.com", member_id="M001")
    member2 = Member(name="Bob Smith", email="bob@example.com", member_id="M002")
    member3 = Member(
        name="Carol White", email="carol@example.com", member_id="M003"
    )

    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)

    # Search for books
    print("\n--- Searching for Books ---")
    print("\nBooks by George Orwell:")
    orwell_books = library.search_book_by_author("George Orwell")
    for book in orwell_books:
        print(f"  - {book.title} ({book.publication_year})")

    print("\nBooks containing 'Pride':")
    pride_books = library.search_book_by_title("Pride")
    for book in pride_books:
        print(f"  - {book.title} by {book.author}")

    # Borrow books
    print("\n--- Borrowing Books ---")
    library.borrow_book("M001", "978-0-06-112008-4")  # Alice borrows To Kill a Mockingbird
    library.borrow_book("M001", "978-0-451-52493-2")  # Alice borrows 1984
    library.borrow_book("M002", "978-0-14-143951-8")  # Bob borrows Pride and Prejudice
    library.borrow_book("M003", "978-0-7432-7356-5")  # Carol borrows The Great Gatsby
    library.borrow_book("M003", "978-0-06-112008-4")  # Carol borrows To Kill a Mockingbird

    # Display books borrowed by a member
    print("\n--- Books Borrowed by Alice ---")
    alice_books = library.get_member_borrowed_books("M001")
    if alice_books:
        for book in alice_books:
            print(f"  - {book['title']} (ISBN: {book['isbn']})")

    # Return a book
    print("\n--- Returning Books ---")
    library.return_book("M001", "978-0-451-52493-2")  # Alice returns 1984
    library.return_book("M002", "978-0-14-143951-8")  # Bob returns Pride and Prejudice

    # Display available books
    print("\n--- Available Books ---")
    available = library.get_available_books()
    for book in available:
        print(
            f"  - {book.title}: {book.available_copies}/{book.total_copies} copies"
        )

    # Display library statistics
    library.display_statistics()

    # Display all books with details
    print("\n--- All Books in Library ---")
    for isbn, book in library.books.items():
        print(f"\n{book}\n")


if __name__ == "__main__":
    main()
