from utils.helpers import getBooksFromFile

"""
    Lists all the available books on the file 'books.txt'
"""
def viewAllBooks() -> None:
    fileBooks = getBooksFromFile()
    print("\n--- Books ---")
    for book in fileBooks:
        status = "Available" if book[3] == "1" else "Unavailable"
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")