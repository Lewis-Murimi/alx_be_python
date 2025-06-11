class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find the book by title and mark it as checked out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Find the book by title and mark it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Print all books that are currently available."""
        available = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        if available:
            for info in available:
                print(info)
        else:
            print("No books available.")
