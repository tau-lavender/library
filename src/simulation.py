import random

from src.library import Library

from src.gen_book import generate_book


"""
добавление новой ĸниги,
удаление случайной ĸниги,
поисĸ по автору/жанру/году,
обновление индеĸса,
попытĸа получить ĸнигу, ĸоторой нет (проверĸа обработĸи
"""


def add_new_books(library):
    print("Добавление книг в доступные")
    print("...")
    book = generate_book()
    count = random.randint(1, 3)
    for _ in range(count):
        library.add_book_in_availiable(book, verbose=False)
    print(f"Добавлено {count} книг {str(book)}")
    print("=Наличие книг в библиотеке=")
    print(library.book_collection_available)


def remove_random_book(library):
    if len(library.book_collection_available) == 0:
        print("В библиотеке нет книг")
        return
    print("Удаление случайной книги/книг из доступных")
    print("...")
    i = random.randint(0, len(library.book_collection_available) - 1)
    book = library.book_collection_available[i]
    if random.random() > 0.5:
        library.remove_book_from_availiable(book, verbose=False)
        print(f"Удалена одна книга {book}")
    else:
        library.remove_book_and_copes_from_availiable(book, verbose=False)
        print(f"Удалены все книги {book}")
    print("=Наличие книг в бибиотеке=")
    print(library.book_collection_available)



events = [
    add_new_books,
    remove_random_book,
]


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    random.seed(seed)
    library = Library()
    print(random.random())
    for step in range(1, steps + 1):
        print(f"---------- start of step {step} ----------")
        random.choice(events)(library)
        print(f"---------- end  of  step {step} ----------")
