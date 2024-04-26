class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability='Available'):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._genre = genre
        self._publication_date = publication_date
        self._availability = availability

    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def publication_date(self):
        return self._publication_date
    
    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, value):
        self._availability = value

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nPublication Date: {self.publication_date}\nAvailability: {self.availability}\n"


    def borrow(self):
        if self._availability == 'Available':
            self._availability = 'Borrowed'
            return True
        else:
            print("This book is not available for borrowing.")
            return False

    def return_book(self):
        if self._availability == 'Borrowed':
            self._availability = 'Available'
            return True
        else:
            print("This book is not currently borrowed.")
            return False



class User:
    def __init__(self, name, library_id, borrowed_books=None):
        self._name = name
        self._library_id = library_id
        self._borrowed_books = borrowed_books if borrowed_books else []

    @property
    def name(self):
        return self._name
    
    @property
    def library_id(self):
        return self._library_id
    
    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    def borrow_book(self, book):
        self._borrowed_books.append(book)
        book.availability = 'Borrowed'
    
    def return_book(self, book):
        self._borrowed_books.remove(book)
        book.availability = 'Available'

    def __str__(self):
        return f"User: {self._name}, Library ID: {self._library_id}, Borrowed Books: {', '.join(book.title for book in self._borrowed_books)}"



class Author:
    def __init__(self, name, biography):
        self._name = name
        self._biography = biography
    
    @property
    def name(self):
        return self._name
    
    @property
    def biography(self):
        return self._biography

    def __str__(self):
        return f"Author: {self._name}, Biography: {self._biography}"



class Genre:
    def __init__(self, name, description):
        self._name = name
        self._description = description
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    def __str__(self):
        return f"Genre: {self._name}, Description: {self._description}"



# Specialized book categories

class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, fiction_type):
        super().__init__(title, author, isbn, genre, publication_date)
        self._fiction_type = fiction_type

    @property
    def fiction_type(self):
        return self._fiction_type
    
    def __str__(self):
        return (super().__str__() + f", Fiction Type: {self._fiction_type}")

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, subject):
        super().__init__(title, author, isbn, genre, publication_date)
        self._subject = subject
    
    @property
    def subject(self):
        return self._subject
    
    def __str__(self):
        return (super().__str__() + f", Subject: {self._subject}")

class MysteryBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, mystery_elements):
        super().__init__(title, author, isbn, genre, publication_date)
        self._mystery_elements = mystery_elements
    
    @property
    def mystery_elements(self):
        return self._mystery_elements
    
    def __str__(self):
        return (super().__str__() + f", Mystery Elements: {self._mystery_elements}")
