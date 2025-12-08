from typing import Iterator


class Book():
    def __init__(self, title: str, author: str | None, year: int | None, genre: str | None, isbn: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __str__(self) -> str:
        return f'"{self.title}" {self.author}'


class BookCollection():
    def __init__(self) -> None:
        self.books: list[Book] = []

    def __getitem__(self, index: int | slice) -> Book | list[Book]:
        if type(index) not in (int, slice):
            raise IndexError(f"Wrong index ({index}) type {type(index)}")
        return self.books[index]

    def __iter__(self) -> Iterator[Book]:
        return iter(self.books)

    def __len__(self) -> int:
        return len(self.books)

    def append(self, book: Book) -> None:
        self.books.append(book)

    def extend(self, books: list[Book]) -> None:
        self.books.extend(books)

    def is_book_exist(self, book: Book) -> bool:
        return book in self.books

    def remove(self, book: Book) -> None:
        if not self.is_book_exist(book):
            raise ValueError(f"{book}")
        self.books.remove(book)
