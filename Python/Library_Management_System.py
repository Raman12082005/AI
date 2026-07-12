# -----------------------------
# Parent Class
# -----------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


# -----------------------------
# Child Class
# -----------------------------
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def borrow_book(self, library, book):
        if library.issue_book(book):
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book}'")
        else:
            print(f"'{book}' is not available.")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.return_book(book)
            print(f"{self.name} returned '{book}'")
        else:
            print("You didn't borrow this book.")

    # Method Overriding
    def display(self):
        print("\nStudent:", self.name)
        print("Borrowed Books:", self.borrowed_books)


# -----------------------------
# Library Class
# -----------------------------
class Library:
    def __init__(self):
        self.books = [
            "Python",
            "Java",
            "C++",
            "Machine Learning",
            "Data Science"
        ]

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def return_book(self, book):
        self.books.append(book)


# -----------------------------
# Main Program
# -----------------------------
library = Library()
student = Student("Ram")

while True:

    print("\n===== Library Menu =====")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Student Details")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.show_books()

    elif choice == "2":
        book = input("Enter book name: ")
        student.borrow_book(library, book)

    elif choice == "3":
        book = input("Enter book name: ")
        student.return_book(library, book)

    elif choice == "4":
        student.display()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")