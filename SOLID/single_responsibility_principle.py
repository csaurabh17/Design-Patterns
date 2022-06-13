# Implementing seperate classes for book properties and book keeping

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


class BookShelf:
    def __init__(self, book, serial, genre):
        self.book = book
        self.serial = serial
        self.genre = genre


b = Book("Famous Five", "Stephen")
bs = BookShelf(b, 1, "Mystery")