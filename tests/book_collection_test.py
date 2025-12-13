import pytest #type: ignore

from src.book import Book
from src.book_collection import BookCollection, BookCollectionUnique


a = Book(isbn=9780451524935,
            title="1984",
            author="George Orwell",
            year=1949,
            genre="Dystopia"
            )

b = Book(isbn=9780451524935,
            title="1984",
            author="George Orwell",
            year=1949,
            genre="Dystopia"
            )

c = Book(isbn=9780441569595,
            title="Neuromancer",
            author="William Gibson",
            year=1984,
            genre="Cyberpunk"
            )

def test_book_collecton_create() -> None:
    coll = BookCollection([a, b, c])
    coll_u = BookCollectionUnique([a, b, c])
    assert coll != coll_u


def test_book_collecton_contains() -> None:
    coll = BookCollection([a])
    coll_u = BookCollectionUnique([a])
    assert a in coll
    assert a in coll_u
    assert c not in coll
    assert c not in coll_u


def test_book_collecton_append() -> None:
    coll = BookCollection()
    coll_u = BookCollectionUnique()
    coll.append(a)
    coll.append(a)
    coll_u.append(a)
    coll_u.append(a)
    assert a in coll
    assert a in coll_u


def test_book_collecton_len() -> None:
    coll = BookCollection()
    coll_u = BookCollectionUnique()
    coll.append(a)
    coll.append(a)
    coll_u.append(a)
    coll_u.append(a)
    assert len(coll) == 2
    assert len(coll_u) == 1


def test_book_collecton_iter() -> None:
    coll = BookCollection([a, b, c])
    iter(coll)
    iter(coll)



def test_book_collecton_getitem() -> None:
    coll = BookCollection([a, b, c])
    assert coll[0] == a
    coll[0:2]
    with pytest.raises(IndexError):
        coll[100]
