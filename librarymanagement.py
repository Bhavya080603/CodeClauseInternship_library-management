class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            author = input("Enter the author of the book to remove: ")
            book = Book(title, author)
            library.remove_book(book)
            print("Book removed successfully!")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
