# ==================================================================================== 
#     PYTHON CLASSWORK — CLASSES AND OBJECTS (CHALLENGING)
# ====================================================================================
#         Topic: Two classes working together — Library system
#         1 Challenging Problem with Solution
# ==============================================================================+=====

# What's new in this challenge:

#   - TWO CLASSES working together
#   - Storing OBJECTS inside another object (a list of books inside
#     a library)
#   - Methods that change state with a CONDITION
#   - Methods that LOOP through a list and count things
#   - Default attribute values set in __init__


# ----------------------------------------------------------------
#                          THE PROBLEM
# ----------------------------------------------------------------

# Library Management System
# -------------------------
# Build a small library system with TWO classes: `Book` and `Library`.

# CLASS 1 — Book
# --------------
# Attributes:
#     title           the book title
#     author          the author's name
#     year            the year published
#     is_borrowed     starts as False (NOT passed in __init__)

# Methods:
#     borrow()
#         If already borrowed: print "Sorry, '<title>' is already borrowed"
#         Otherwise: set is_borrowed = True, print "You borrowed '<title>'"

#     return_book()
#         If not borrowed: print "'<title>' was not borrowed"
#         Otherwise: set is_borrowed = False, print "You returned '<title>'"

#     show()
#         Print: <title> by <author> (<year>) - <status>
#         where status is "Available" or "Borrowed"


# CLASS 2 — Library
# -----------------
# Attributes:
#     name            the library's name
#     books           a list of Book objects (starts empty)

# Methods:
#     add_book(book)
#         Append the book to self.books
#         Print "Added '<book.title>' to <library name>"

#     show_all()
#         Print "=== <library name> ==="
#         Then call show() on every book in the library

#     count_available()
#         Return how many books are NOT borrowed


# YOUR MAIN CODE — Do this in order:
# 1. Create a library:
#        lib = Library("Tuwaiq Library")

# 2. Create 3 books:
#        b1 = Book("Clean Code", "Robert Martin", 2008)
#        b2 = Book("Python Crash Course", "Eric Matthes", 2019)
#        b3 = Book("The Pragmatic Programmer", "Andy Hunt", 1999)

# 3. Add all three to the library.

# 4. Show all books.

# 5. Borrow b1, try to borrow b1 AGAIN (should fail), then
#    return it.

# 6. Print "Available books: <count>" using count_available().

# 7. Show all books one more time.

#============================================================================================
# Solution:
#============================================================================================

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == True:
            print(f"Sorry, '{self.title}' is already borrowed")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'")

    def return_book(self):
        if self.is_borrowed == False:
            print(f"'{self.title}' was not borrowed")
        else:
            self.is_borrowed = False
            print(f"You returned '{self.title}'")

    def show(self):
        if self.is_borrowed == True:
            status = "Borrowed"
        else:
            status = "Available"
        print(f"{self.title} by {self.author} ({self.year}) - {status}")


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}")

    def show_all(self):
        print(f"=== {self.name} ===")
        for book in self.books:
            book.show()

    def count_available(self):
        count = 0
        for book in self.books:
            if book.is_borrowed == False:
                count += 1
        return count



lib = Library("Tuwaiq Library")

b1 = Book("Clean Code", "Robert Martin", 2008)
b2 = Book("Python Crash Course", "Eric Matthes", 2019)
b3 = Book("The Pragmatic Programmer", "Andy Hunt", 1999)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print()
lib.show_all()
print()
b1.borrow()
b1.borrow()
b1.return_book()
print()
print(f"Available books: {lib.count_available()}")
print()
lib.show_all()