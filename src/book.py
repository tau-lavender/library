

class Book():
    def __init__(self, title: str, author: str | None, year: int | None, genre: str | None, isbn: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


class BookCollection():
    def __init__(self):
        self.books: list[Book] = []

    def __getitem__(self, index: int | slice):
        if type(index) not in (int, slice):
            raise IndexError(f"Wrong index ({index}) type {type(index)}")
        return self.books[index]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.books)

    def add_book(self, book: Book):
        self.books.append(book)

    def add_books(self, books: list[Book]):
        self.books.extend(books)

    def is_book_exist(self, book: Book):
        return book in self.books

    def remove(self, book: Book):
        if not self.is_book_exist(book):
            raise ValueError(f"{book}")
        return self.books.remove(book)
