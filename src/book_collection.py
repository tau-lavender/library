from typing import (
    Iterator,
    List
)
from src.book import Book


class BookCollection():
    def __init__(self, data: List[Book] | None = None) -> None:
        self.books: List[Book] = [] if data is None else data.copy()


    def __contains__(self, book: Book) -> bool:
        return book in self.books


    @classmethod
    def new_collection_from_list(cls, data: List[Book]) -> BookCollection:
        return cls(data = data)


    def __getitem__(self, index: int | slice) -> Book | BookCollection:
        if type(index) not in (int, slice):
            raise IndexError(f"Wrong index ({index}) type {type(index)}")
        if isinstance(index, int):
            return self.books[index]
        if isinstance(index, slice):
            return self.new_collection_from_list(self.books[index])


    def __iter__(self) -> Iterator[Book]:
        return iter(self.books)


    def __len__(self) -> int:
        return len(self.books)


    def count(self, book) -> int:
        return self.books.count(book)


    def append(self, book: Book) -> None:
        self.books.append(book)


    def extend(self, books: List[Book]) -> None:
        self.books.extend(books)


    def remove(self, book: Book) -> None:
        if book not in self:
            raise ValueError(f"{book}")
        self.books.remove(book)


class BookCollectionUnique(BookCollection):
    """
    Только уникальные книги
    """

    def append(self, book: Book) -> None:
        if book not in self:
            self.books.append(book)

    def extend(self, books: List[Book]) -> None:
        for book in books:
            self.append(book)
