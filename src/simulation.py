import random

from src.library import Library
from src.gen_book import generate_book, generate_random_search_prompt

from typing import Any


"""
TODO
добавление новой ĸниги,                                    X
удаление случайной ĸниги,                                  X
получение книги,                                           X
поиск + получение книги                                    X
попытĸа получить ĸнигу, ĸоторой нет                        X
возврат книги                                              X
возврат книги которую не брали                             X
"""


def add_new_books(library):
    print("> Event: Добавление книг в доступные")
    print("...")
    book = generate_book()
    count = random.randint(1, 3)
    for _ in range(count):
        library.add_book_in_availiable(book, verbose=False)
    print(f"Добавлено {count} книг {str(book)}")
    print("=Наличие книг в библиотеке=")
    print(library.book_collection_available)


def remove_random_book(library):
    print("> Event: Удаление случайной книги/книг из доступных")
    print("...")
    if len(library.book_collection_available) == 0:
        print("В библиотеке нет книг")
        return
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


def give_out_book_wo_search(library):
    print("> Event: Пользователь получает книгу без поиска ", end = "")
    book_exist = True
    if random.random() > 0.5:
        book_exist = False
        print("(несуществующую)")
    else:
        print("(существующую)")
    print("...")
    if len(library.book_collection_available) == 0:
        print("В библиотеке нет книг")
        return

    if book_exist:
        i = random.randint(0, len(library.book_collection_available) - 1)
        random_book = library.book_collection_available[i]
    else:
        random_book = generate_book()

    print(f"Пользователь хочет получить книгу {random_book}")
    library.give_out_book(random_book)


def search_for_book_and_give_it(library):
    print("> Event: Пользователь ищет книгу ", end="")
    book_exist = True
    if random.random() > 0.5:
        book_exist = False
        print("(несуществующую)")
    else:
        print("(существующую)")

    if len(library.book_collection_available) == 0:
        print("В библиотеке нет книг")
        return

    if book_exist:
        isbn = None
        author = None
        year = None
        i = random.randint(0, len(library.book_collection_available) - 1)
        random_book_data = library.book_collection_available[i]

        while isbn is None and author is None and year is None:
            if random.random() > 0.5:
                isbn = random_book_data.isbn
            if random.random() > 0.5:
                author = random_book_data.author
            if random.random() > 0.5:
                year = random_book_data.year
    else:
        d = generate_random_search_prompt()
        isbn = d["isbn"]
        author = d["author"]
        year = d["year"]


    print(f"""Пользователь хочет книгу c
        isbn: {str(isbn) if isbn is not None else "не важно каким"}
        автором: {str(author) if author is not None else "не важно каким"}
        годом издания: {str(year) if year is not None else "не важно каким"}""")
    print("Поиск")
    print("...")
    result = library.search(isbn=isbn, author=author, year=year)
    if len(result) == 0:
        print("Не найдено подходящей книги")
        return
    elif len(result) == 1:
        user_want_book = result[0]
        print("Найдена книга: ", end="")
    else:
        print("Найденно несколько книг подходящих под запрос")
        user_choise = random.randint(0, len(result) - 1)
        user_want_book = result[user_choise]
        print("Пользователь выбрал книгу: ", end="")
    print(f"{user_want_book}")
    print(f"Данные книги: {str(user_want_book)} isbn: {user_want_book.isbn} year: {result[0].year} genre: {result[0].genre}")
    library.give_out_book(user_want_book)


def get_book(library):
    print("> Event: Пользователь сдаёт книгу ", end="")
    book_exist = True
    if random.random() > 0.5:
        book_exist = False
        print("(которую не забирали)")
    else:
        print("(которую забирали)")
    print("...")
    if len(library.book_collection_on_hand) == 0:
        print("Все забранные книги были возвращены или книги не забирали")
        return
    if book_exist:
        i = random.randint(0, len(library.book_collection_on_hand) - 1)
        book = library.book_collection_on_hand[i]
    else:
        book = generate_book()

    print(f"Пользователь хочет сдать книгу {book}")
    library.get_book(book)



events = {
    add_new_books: 0,
    remove_random_book: 0,
    give_out_book_wo_search: 0,
    search_for_book_and_give_it: 0,
    get_book: 0
}


def run_simulation(steps: int = 20, seed: Any = None) -> None:
    random.seed(seed)
    library = Library()
    print("\n" * 100)
    print("---- Добавление книг перед симуляцией ----")
    for _ in range(3):
        add_new_books(library)
    print("------------ Начало симуляции ------------")
    for step in range(1, steps + 1):
        input("Нажмите ENTER для следующего шага")
        print(f"---------- start of step {step} ----------")
        event = random.choice(list(events.keys()))
        events[event] += 1
        event(library)
        print(f"---------- end  of  step {step} ----------")
    print("------------ Конец  симуляции ------------")
    print("=Наличие книг в бибиотеке=")
    print(library.book_collection_available)
    print()
    print("=Забраные книги из бибиотеки=")
    print(library.book_collection_on_hand)
    print()
    print("Вызваны ивенты:")
    for event in events:
        print(f"Ивент {event.__name__} вызван {events[event]} раз")
