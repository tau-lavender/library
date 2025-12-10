from src.book import Book

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

def test_book_temp_str() -> None:
    assert a._get_temp_str() == b._get_temp_str()

def test_book_eq_ne() -> None:
    assert a == b
    assert not a != b
    assert not a == c
    assert a != c

def test_book_str_repr() -> None:
    assert str(a) == str(b)
    assert repr(a) == repr(b)
