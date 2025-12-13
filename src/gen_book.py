import random
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

def generate_book():
    return Book(
        isbn=random.randint(900_00000_00000, 999_99999_99999),
        title=random.choice(titles),
        author=random.choices([random.choice(authors), None], cum_weights=[10, 1])[0],
        year=random.choices([random.randint(1800, 2025), None], cum_weights=[10, 1])[0],
        genre=random.choices([random.choice(genres), None], cum_weights=[10, 1])[0],
    )
