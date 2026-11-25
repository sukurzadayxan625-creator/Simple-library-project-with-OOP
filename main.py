from book import Book
from student import Student
from libary import Library


def main():
    library = Library("My Library")

    library.addBook(Book(1, "Clean Code", "Robert Martin", 464))
    library.addBook(Book(2, "Python Crash Course", "Eric Matthes", 560))
    library.addBook(Book(3, "Atomic Habits", "James Clear", 320))

    library.addStudent(Student(1, "Taleh"))
    library.addStudent(Student(2, "Ramiz"))
    library.addStudent(Student(3, "Ramal"))

    while True:
        print(f"\n--- {library.name} ---")
        print("1. Show books")
        print("2. Show students")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.showBooks()
        elif choice == "2":
            library.showStudents()
        elif choice == "3":
            try:
                studentID = int(input("Student ID: "))
                bookID = int(input("Book ID: "))
                library.borrowBook(studentID, bookID)
            except ValueError:
                print("Please enter a number for the IDs.")
        elif choice == "4":
            try:
                studentID = int(input("Student ID: "))
                bookID = int(input("Book ID: "))
                library.returnBook(studentID, bookID)
            except ValueError:
                print("Please enter a number for the IDs.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
