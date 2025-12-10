
class Book():
    def __init__(self,
                isbn: int,
                title: str,
                author: str | None = None,
                year: int | None = None,
                genre: str | None = None
                ) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre


    def _get_temp_str(self):
        return str(self.isbn) + str(self.title) + str(self.author) + str(self.year) + str(self.genre)


    def hash(self):
        return hash(self._get_temp_str())


    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Book):
            return False
        return self._get_temp_str() == value._get_temp_str()


    def __str__(self) -> str:
        return f'"{self.title}" {self.author}'


    def __repr__(self) -> str:
        return f'Book: ({self.isbn}) "{self.title}" {self.author} {self.year} {self.genre}'
