from utils.helpers import getBooksFromFile, writeToBooks, USERS_PATH

"""
    Walks the user through the loaning process.
"""

def loanBook() -> None:
    booksFromFile = getBooksFromFile()
    bookId = input("What's the book's ID? ")
    userId = input("What's the ID of the user? ")
    
    users = []
    with open(USERS_PATH, "r") as file:
        for line in file:
            users.append(line.strip().split(";"))
            
    foundUser = False
    for user in users:
        if user[0] == userId:
            foundUser = True
            if user[2] == "1":
                print("This user reached his book loan limit. Choose another person.")
                return
            break
            
    if not foundUser:
        print("User not found.")
        return

    didChange = False
    for book in booksFromFile:
        if book[0] == bookId:
            if book[3] == "1":
                book[3] = "0"
                didChange = True
                for user in users:
                    if user[0] == userId:
                        user[2] = "1"
                print("Your loan was successful, enjoy!")
            else:
                print("Book already taken. Choose another book.")
            break
            
    if didChange:
        writeToBooks(booksFromFile)
        with open(USERS_PATH, "w") as file:
            for user in users:
                file.write(";".join(user) + "\n")

"""
    Walks the user through the process of returning his loaned books.
"""

def returnBook() -> None:
    booksFromFile = getBooksFromFile()
    bookId = input("What's the book's ID? ")
    userId = input("What's the ID of the user? ")
    
    users = []
    with open(USERS_PATH, "r") as file:
        for line in file:
            users.append(line.strip().split(";"))

    didChange = False
    for book in booksFromFile:
        if book[0] == bookId:
            if book[3] == "0":
                book[3] = "1"
                didChange = True
                for user in users:
                    if user[0] == userId:
                        user[2] = "0"
                print("Thank you for loaning with us. See you soon!")
            else:
                print("This book wasn't loaned. Choose another one.")
            break
            
    if didChange:
        writeToBooks(booksFromFile)
        with open(USERS_PATH, "w") as file:
            for user in users:
                file.write(";".join(user) + "\n")