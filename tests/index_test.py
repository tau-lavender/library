from src.index import IndexDict
from src.book import Book
from src.book_collection import BookCollectionUnique


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

def test_index() -> None:
    ind: IndexDict = IndexDict()
    assert type(str(ind)) is str
    assert type(repr(ind)) is str
    iter(ind)
    assert len(ind) == 0
    ind["123"] = a
    assert ind["123"][0] == a
    assert isinstance(ind["123"], BookCollectionUnique)
    assert len(ind) == 1
    ind.keys()
    ind.values()
    ind.items()
    ind["123"].append(c)
    assert len(ind) == 1
    assert len(ind["123"]) == 2
    ind.remove_book("123", a)
    assert len(ind) == 1
    assert len(ind["123"]) == 1
    assert ind["123"][0] == c
