from typing import (
    Iterator,
    List
)


class Book():
    def __init__(self,
                isbn: int,
                title: str,
                author: str | None = None,
                year: int | None = None,
                genre: str | None = None
                ) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre


    def _get_temp_str(self):
        return str(self.isbn) + str(self.title) + str(self.author) + str(self.year) + str(self.genre)


    def hash(self):
        return hash(self._get_temp_str())


    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Book):
            return False
        return self._get_temp_str() == value._get_temp_str()


    def __str__(self) -> str:
        return f'"{self.title}" {self.author}'


    def __repr__(self) -> str:
        return f'Book: ({self.isbn}) "{self.title}" {self.author} {self.year} {self.genre}'


class BookCollection():
    def __init__(self) -> None:
        self.books: List[Book] = []


    def __contains__(self, book: Book) -> bool:
        return book in self.books


    def __getitem__(self, index: int | slice) -> Book | List[Book]:
        if type(index) not in (int, slice):
            raise IndexError(f"Wrong index ({index}) type {type(index)}")
        return self.books[index]


    def __iter__(self) -> Iterator[Book]:
        return iter(self.books)


    def __len__(self) -> int:
        return len(self.books)


    def append(self, book: Book) -> None:
        self.books.append(book)


    def extend(self, books: List[Book]) -> None:
        self.books.extend(books)


    def remove(self, book: Book) -> None:
        if book not in self:
            raise ValueError(f"{book}")
        self.books.remove(book)
