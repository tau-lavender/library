from typing import (
    Iterator,
    List
)
from src.book import Book


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
