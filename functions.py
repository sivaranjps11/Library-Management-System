# STEP 1: BOOK CLASS
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__copies = copies

    def available_copies(self):
        return self.__copies

    def issue(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False

    def give_back(self):
        self.__copies += 1

    def __str__(self):
        return f"{self.book_id} | {self.title} by {self.author} | Copies: {self.__copies}"

# STEP 2: MEMBER CLASS

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = []

    def max_books(self):
        return 1

    def member_type(self):
        return "Member"

    def can_borrow(self):
        return len(self.borrowed) < self.max_books()

    def __str__(self):
        return f"{self.member_id} | {self.name} | {self.member_type()} | Borrowed: {len(self.borrowed)}/{self.max_books()}"

# STUDENT CLASS

class Student(Member):
    def max_books(self):
        return 2

    def member_type(self):
        return "Student"

# TEACHER CLASS

class Teacher(Member):
    def max_books(self):
        return 4

    def member_type(self):
        return "Teacher"

# STEP 3: LIBRARY CLASS

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def load_books(self, data):
        for book_id, details in data.items():
            self.books[book_id] = Book(
                book_id,
                details["title"],
                details["author"],
                details["copies"]
            )

    def load_members(self, data):
        for details in data:
            if details["type"] == "teacher":
                member = Teacher(details["id"], details["name"])
            else:
                member = Student(details["id"], details["name"])

            self.members[details["id"]] = member

    def issue_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"

        if book_id not in self.books:
            return "Book not found"

        member = self.members[member_id]
        book = self.books[book_id]

        if not member.can_borrow():
            return f"{member.name} has reached the limit"

        if not book.issue():
            return f"{book.title} is not available"

        member.borrowed.append(book_id)

        return f"{member.name} issued {book.title}"

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"

        if book_id not in self.books:
            return "Book not found"

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed:
            return "Cannot return"

        member.borrowed.remove(book_id)
        book.give_back()

        return f"{member.name} returned {book.title}"

    def show_books(self):
        for book in self.books.values():
            print(book)

    def show_members(self):
        for member in self.members.values():
            print(member)