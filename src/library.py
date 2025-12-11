from src.book import Book
from src.book_collection import BookCollection
from src.index import IsbnIndexDict, AuthorIndexDict, YearIndexDict
# from typing import List


class Library():
    def __init__(self) -> None:
        self.book_collection_available = BookCollection()
        self.book_collection_on_hand = BookCollection()
        self.isbn_dict = IsbnIndexDict()
        self.author_dict = AuthorIndexDict()
        self.year_dict = YearIndexDict()


    def add_book_in_availiable(self, book: Book, verbose: bool = True) -> None:
        self.book_collection_available.append(book)

        if book.isbn not in self.isbn_dict.keys():
            self.isbn_dict[book.isbn] = set([book])

        if book.author not in self.author_dict.keys():
            self.author_dict[book.author] = set()
        self.author_dict[book.author].add(book)

        if book.year not in self.year_dict.keys():
            self.year_dict[book.year] = set()
        self.year_dict[book.year].add(book)

        if verbose:
            print(f"Добавлена книга {str(book)}")


    def remove_book_from_availiable(self, book: Book, verbose: bool = True) -> None:
        if book not in self.book_collection_available:
            if verbose:
                print(f"Книги {str(book)} нет в библиотеке")
            return

        self.book_collection_available.remove(book)

        if book not in self.book_collection_available:
            self.isbn_dict.remove_book(book.isbn, book)
            self.author_dict.remove_book(book.isbn, book)
            self.isbn_dict.remove_book(book.isbn, book)

        if verbose:
            print(f"Экземпляр книги {str(book)} убран")


    def remove_book_and_copes_from_availiable(self, book: Book, verbose: bool = True) -> None:
        while book in self.book_collection_available:
            self.remove_book_from_availiable(book, verbose=False)

        if verbose:
            print(f"Все экземпляры книги {str(book)} убраны")


    def give_out_book(self, book: Book, verbose: bool = True) -> None:
        if book not in self.book_collection_available:
            if verbose:
                print(f"Книги {str(book)} нет в библиотеке")
            return

        self.remove_book_from_availiable(book)
        self.book_collection_on_hand.append(book)


    def get_book(self, book: Book, verbose:bool = True) -> None:
        if book not in self.book_collection_on_hand:
            if verbose:
                print(f"Книгу {str(book)} не забирали, или она была удалена из коллекции. Книгу нельзя принять")
            return
        else:
            self.add_book_in_availiable(book)
            self.book_collection_on_hand.remove(book)


    # def search(self, isbn: int | None, author: str | None, year: int | None) -> List[Book]:
    #     ...
