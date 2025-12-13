import random
from typing import Dict
from src.book import Book

# список рандомных названий взятых из англ вики
titles = [
    "Neuromancer",
    "1984",
    "All Systems Red",
    "Ambassador",
    "Angel Station",
    "Another Word",
    "Artificial Condition",
    "The Authorities"
]
authors = [
    "Mark Twain",
    "Edgar Allan Poe",
    "Louise Glück",
    "Ernest Hemingway",
    "George Orwell",
    "William Gibson",
    "Alexander Pushkin",
    "Nikolai Gogol",
    "Ivan Turgenev",
    "Fyodor Dostoevsky",
    "Leo Tolstoy",
]
genres = [
    "fairy tale",
    "heroic",
    "myth",
    "drama",
    "novel",
    "adventure",
    "crime",
    "science fiction",
    "hilosophy"
]

def generate_book() -> Book:
    return Book(
        isbn=random.randint(900_00000_00000, 999_99999_99999),
        title=random.choice(titles),
        author=random.choice(authors),
        year=random.randint(1800, 2025),
        genre=random.choice(genres)
    )

def generate_random_search_prompt() -> Dict[str, int | str | None]:
    return {
        "isbn": random.choice([random.randint(900_00000_00000, 999_99999_99999), None]),
        "author": random.choice([random.choice(authors), None]),
        "year": random.choice([random.randint(1800, 2025), None])
    }
