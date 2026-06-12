import sys
sys.dont_write_bytecode = True #notopycache

from app import fetchFuncs, modifyFuncs
from utils.helpers import setup, clear

def main():
    setup()
    while True:
        print("\n=== Library Management System ===")
        print("1 - View books")
        print("2 - Loan a book")
        print("3 - Return a book")
        print("4 - Logout")
        opt = input("-> ")
        
        if opt == "1":
            clear()
            fetchFuncs.viewAllBooks()
        elif opt == "2":
            clear()
            modifyFuncs.loanBook()
        elif opt == "3":
            clear()
            modifyFuncs.returnBook()
        elif opt == "4":
            clear()
            print("Come back soon! :-)\n")
            break
        else:
            clear()
            print("Please, choose a valid option.")

if __name__ == "__main__":
    main()