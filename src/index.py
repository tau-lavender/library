from src.book import Book
from typing import (
    Iterator,
    TypeVar,
    KeysView,
    ItemsView,
    ValuesView,
    Dict,
    Tuple,
    Union
)

_KT = TypeVar("_KT")
_VT = Union[Book, set[Book]]


class IndexDict[_KT]:
    def __init__(self) -> None:
        self.dict: Dict[_KT, _VT] = dict()


    def __str__(self) -> str:
        return str(self.dict)


    def __repr__(self) -> str:
        return str(self.dict)


    def __iter__(self) -> Iterator[_KT]:
        return iter(self.dict)


    def __len__(self) -> int:
        return len(self.dict)


    def __getitem__(self, key: _KT) -> _VT:
        return self.dict[key]


    def __setitem__(self, key: _KT, item: _VT):
        self.dict[key] = item


    def keys(self) -> KeysView[_KT]:
        return self.dict.keys()


    def values(self) -> ValuesView[_VT]:
        return self.dict.values()


    def items(self) -> ItemsView[_KT, _VT]:
        return self.dict.items()


    def pop(self, key: _KT) -> _VT:
        return self.dict.pop(key)


    def popitem(self) -> Tuple[_KT, _VT]:
        return self.dict.popitem()


    def clear(self) -> None:
        self.dict.clear()


class IsbnIndexDict(IndexDict):
    def __init__(self):
        _KT = int
        super.__init__()


class AuthorIndexDict(IndexDict):
    def __init__(self):
        _KT = Union[str, None]
        super.__init__()


class YearIndexDict(IndexDict):
    def __init__(self):
        _KT = Union[int, None]
        super.__init__()
