from book import Book


class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.borrowedBooks = []

    def showInfo(self):
        print(f"""
ID: {self.studentID}
Name: {self.name}
Borrowed books: {len(self.borrowedBooks)}
""")

    def borrowBook(self, book):
        if book.isAvailable:
            book.borrow()
            self.borrowedBooks.append(book)
        else:
            print("Book is not available...")

    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print("This student has not borrowed this book.")
