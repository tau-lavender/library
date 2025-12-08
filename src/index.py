

class Index():
    def __init__(self, isbn: int | None, author: str | None, year: int | None) -> None:
        self.isbn = isbn
        self.author = author
        self.year = year


    def __str__(self) -> str:
        return f'index: {self.isbn}, {self.author}, {self.year}'
