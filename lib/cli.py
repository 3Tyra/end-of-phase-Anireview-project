import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helpers import (
    exit_program,
    list_anime,
    add_anime,
    delete_anime,
    list_studios,
    add_review
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_anime()
        elif choice == "2":
            add_anime()
        elif choice == "3":
            delete_anime()
        elif choice == "4":
            list_studios()
        elif choice == "5":
            add_review()
        else:
            print("Invalid choice")


def menu():
    print("Anime Review CLI")
    print("0. Exit")
    print("1. List all anime")
    print("2. Add new anime")
    print("3. Delete anime")
    print("4. List studios")
    print("5. Add review")


if __name__ == "__main__":
    main()
