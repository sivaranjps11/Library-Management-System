from functions import Library

# STARTER DATA
books_data = {
    "B101": {"title": "Python Basics", "author": "Anu", "copies": 2},
    "B102": {"title": "Data Science 101", "author": "Binu", "copies": 1},
    "B103": {"title": "AWS Guide", "author": "Cathy", "copies": 3},
    "B104": {"title": "Statistics Made Easy", "author": "Dev", "copies": 1},
}
members_data = [
    {"id": "M1", "name": "Anu", "type": "student"},
    {"id": "M2", "name": "Binu", "type": "teacher"},
    {"id": "M3", "name": "Cathy", "type": "student"},
]
# CREATE LIBRARY OBJECT

library = Library()
library.load_books(books_data)
library.load_members(members_data)

# TASK 1: BOOK CATALOGUE
print("Task 1: Book catalogue")
library.show_books()

# TASK 2: MEMBERS AND INHERITANCE

print("\nTask 2: Members")
library.show_members()

# TASK 3: ISSUE BOOKS

print("\nTask 3: Issue books")
print(library.issue_book("M1", "B101"))
print(library.issue_book("M1", "B102"))
print(library.issue_book("M1", "B103"))
print(library.issue_book("M3", "B102"))
print(library.issue_book("M3", "B999"))

# TASK 4: TEACHER BORROWS

print("\nTask 4: Teacher borrows")
print(library.issue_book("M2", "B101"))
print(library.issue_book("M2", "B103"))
print(library.issue_book("M2", "B104"))
print(library.issue_book("M2", "B102"))
print(library.members["M2"])

# TASK 5: RETURN BOOKS

print("\nTask 5: Return books")
print(library.return_book("M1", "B102"))
print(library.return_book("M1", "B102"))
print(library.issue_book("M3", "B102"))

# TASK 6: FINAL STATUS

print("\nTask 6: Final status")
library.show_books()
library.show_members()

total_books = sum(
    len(member.borrowed)
    for member in library.members.values()
)

print("Books on loan:", total_books)