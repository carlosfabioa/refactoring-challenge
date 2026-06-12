import os
from pathlib import Path

"""
    Constants that will be used across the utils and app modules.
"""

ROOT_DIR = str(Path(__file__).parent.parent)

USERS_PATH = os.path.join(ROOT_DIR + "\\db\\users.txt")
BOOKS_PATH = os.path.join(ROOT_DIR + "\\db\\books.txt")
print(ROOT_DIR)

"""
    Initial setup for creating the files 'books.txt' and 'users.txt'.

    Those files are used as a "database", to store data.

    Both files start with initial data, more specifically 2.
"""

def setup() -> None:
    if not os.path.exists(BOOKS_PATH):
        with open(BOOKS_PATH, "w") as f:
            f.write("1;O Alquimista;Paulo Coelho;1\n2;1984;George Orwell;0\n")
            
    if not os.path.exists(USERS_PATH):
        with open(USERS_PATH, "w") as f:
            f.write("1;Joao;1\n2;Maria;0\n")

"""
    Gets all the books from the file 'books.txt' and pushes them onto a list.

    Returns:
        books: A list containing all the books from the file 'books.txt'
"""

def getBooksFromFile() -> list:
    books = []
    if os.path.exists(BOOKS_PATH):
        with open(BOOKS_PATH, "r") as f:
            for l in f:
                if l.strip():
                    books.append(l.strip().split(";"))
    return books

"""
    Writes a list of lists to 'books.txt'

    Args:
        books: The list of iterables to be wrote onto the file 'books.txt'
"""

def writeToBooks(books) -> None:
    with open(BOOKS_PATH, "w") as f:
        for q in books:
            f.write(";".join(q) + "\n")

"""
    Clears the user's terminal
"""

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    return