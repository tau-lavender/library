from src.book import Book
from src.book_collection import BookCollection, BookCollectionUnique
from src.index import IsbnIndexDict, AuthorIndexDict, YearIndexDict


class Library():
    """
    Класс библиотеки
    Хранит:
    Коллекцию книг в библиотеке,
    Коллекцию выданных книг,
    Индексацию по ISBN, Author, Year
    Методы влияют на все коллеции
    """

    def __init__(self) -> None:
        self.book_collection_available = BookCollection()
        self.book_collection_on_hand = BookCollection()
        self.isbn_dict = IsbnIndexDict()
        self.author_dict = AuthorIndexDict()
        self.year_dict = YearIndexDict()


    def add_book_in_availiable(self, book: Book, verbose: bool = True) -> None:
        """
        Добавляет книгу в доступные и создаёт/добавляет в коллекции в индексации
        :book: объект класса Book для добавления
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        self.book_collection_available.append(book)
        if book.isbn not in self.isbn_dict.keys():
            self.isbn_dict[book.isbn] = BookCollectionUnique()
        self.isbn_dict[book.isbn].append(book)

        if book.author not in self.author_dict.keys():
            self.author_dict[book.author] = BookCollectionUnique()
        self.author_dict[book.author].append(book)

        if book.year not in self.year_dict.keys():
            self.year_dict[book.year] = BookCollectionUnique()
        self.year_dict[book.year].append(book)

        if verbose:
            print(f"Добавлена книга {str(book)}")


    def remove_book_from_availiable(self, book: Book, verbose: bool = True) -> None:
        """
        Убирирает книгу из доступных и убирет из коллекции в индексации
        :book: объект класса Book для удаления
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        if book not in self.book_collection_available:
            if verbose:
                print(f"Книги {str(book)} нет в библиотеке")
            return

        self.book_collection_available.remove(book)

        if book not in self.book_collection_available:
            self.isbn_dict.remove_book(book.isbn, book)
            self.author_dict.remove_book(book.author, book)
            self.year_dict.remove_book(book.year, book)

        if verbose:
            print(f"Экземпляр книги {str(book)} убран")


    def remove_book_and_copes_from_availiable(self, book: Book, verbose: bool = True) -> None:
        """
        Удаляет все одинаковые книги book через remove_book_from_availiable
        :book: объект класса Book для удаления
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        while book in self.book_collection_available:
            self.remove_book_from_availiable(book, verbose=False)

        if verbose:
            print(f"Все экземпляры книги {str(book)} убраны")


    def give_out_book(self, book: Book, verbose: bool = True) -> None:
        """
        Выдаёт book
        Удаляет из доступных, добаляет в "на руках"
        :book: объект класса Book для dslfxb
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        if book not in self.book_collection_available:
            if verbose:
                print(f"Книги {str(book)} нет в библиотеке")
            return

        self.remove_book_from_availiable(book, verbose=False)
        self.book_collection_on_hand.append(book)
        if verbose:
            print(f"Выдана книга {book}")


    def get_book(self, book: Book, verbose:bool = True) -> None:
        """
        Возвращает book в коллецию, удаляет из "на руках"
        :book: объект класса Book для djpdhfotybz
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        if book not in self.book_collection_on_hand:
            if verbose:
                print(f"Книгу {str(book)} не забирали, или она была удалена из коллекции. Книгу нельзя принять")
            return
        else:
            self.add_book_in_availiable(book, verbose=False)
            self.book_collection_on_hand.remove(book)
            if verbose:
                print(f"Сдана книга {book}")


    def search(self,
               isbn: int | None = None,
               author: str | None = None,
               year: int | None = None,
               verbose: bool = True
               ) -> BookCollectionUnique:
        """
        Поиск по индексам
        :isbn: данные для поиска, если None не влияет
        :author: данные для поиска, если None не влияет
        :year: данные для поиска, если None не влияет
        :verbose: True для вывода информации в консоль, False для отключения
        :return: None
        """
        ans: BookCollectionUnique = BookCollectionUnique()
        temp_ans: BookCollectionUnique = BookCollectionUnique()
        if isbn is None and author is None and year is None:
            if verbose:
                print("Не указанны параметры для поиска")
            return ans

        if isbn is not None:
            if isbn not in self.isbn_dict.keys():
                if verbose:
                    print(f"Не найдено книг с isbn: {isbn}")
                return ans
            temp_ans.extend(self.isbn_dict[isbn])

        if author is not None:
            if author not in self.author_dict.keys():
                if verbose:
                    print(f"Не найдено книг от автора: {author}")
                return ans
            temp_ans.extend(self.author_dict[author])
        if year is not None:
            if year not in self.year_dict.keys():
                if verbose:
                    print(f"Не найдено книг с годом издания: {year}")
                return ans
            temp_ans.extend(self.year_dict[year])

        for book in temp_ans:
            if book.isbn == isbn or isbn is None:
                if book.author == author or author is None:
                    if book.year == year or year is None:
                        ans.append(book)

        return ans
