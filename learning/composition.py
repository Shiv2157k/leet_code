from typing import List


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


if __name__ == "__main__":
    book = Book("Harry Potter")
    book1 = Book("Python 101")
    shelf = BookShelf(book, book1)
    print(shelf)