from classes import *
import re
import json


books = []
users = []
authors = []
genres = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")

    while not valid_isbn(isbn):
        print("Invalid ISBN format. ISBN must be 10 or 13 digits.")
        isbn = input("Enter book ISBN: ")
    genre = input("Enter book genre: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    
    while not valid_publication_date(publication_date):
        print("Invalid date format. Date must be in the format YYYY-MM-DD.")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
    book_type = input("Enter book type (Fiction, Non-Fiction, Mystery): ")

    while not valid_book_type(book_type):
        print("Invalid book type. Enter 'Fiction', 'Non-Fiction', or 'Mystery'.")
        book_type = input("Enter book type (Fiction, Non-Fiction, Mystery): ")

    if book_type == "Fiction":
        fiction_type = input("Enter fiction type: ")
        new_book = FictionBook(title, author, isbn, genre, publication_date, fiction_type)
    elif book_type == "Non-Fiction":
        subject = input("Enter subject: ")
        new_book = NonFictionBook(title, author, isbn, genre, publication_date, subject)
    elif book_type == "Mystery":
        mystery_elements = input("Enter mystery elements: ")
        new_book = MysteryBook(title, author, isbn, genre, publication_date, mystery_elements)
    else:
        new_book = Book(title, author, isbn, genre, publication_date)
    books.append(new_book)
    save_data_to_file(books, 'books.json')
    print("Book added successfully!")


def display_all_books():
    global books
    print("Number of books loaded:", len(books))
    if books:
        for book in books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            print("Genre:", book.genre)
            print("Publication Date:", book.publication_date)
            print("Availability:", book.availability)
            print()
    else:
        print("No books available.")


def add_user():
    name = input("Enter user name: ")
    while not valid_name(name):
        print("Invalid name format. Name should only contain letters and spaces.")
        name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    while not valid_library_id(library_id):
        print("Invalid library ID format. Library ID must be numeric.")
        library_id = input("Enter library ID: ")
    new_user = User(name, library_id)
    users.append(new_user)
    save_data_to_file(users, 'users.json')
    print("User added successfully!")

def display_all_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")

def add_author():
    name = input("Enter author name: ")
    while not valid_name(name):
        print("Invalid name format. Name should only contain letters and spaces.")
        name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    new_author = Author(name, biography)
    authors.append(new_author)
    save_data_to_file(authors, 'authors.json')
    print("Author added successfully!")

def display_all_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors available.")

def add_genre():
    name = input("Enter genre name: ")
    while not valid_name(name):
        print("Invalid genre name. Genre name should only contain letters and spaces.")
        name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    while not valid_description(description):
        print("Invalid description. Description cannot be empty.")
        description = input("Enter genre description: ")
    new_genre = Genre(name, description)
    genres.append(new_genre)
    save_data_to_file(genres, 'genres.json')
    print("Genre added successfully!")

def display_all_genres():
    if genres:
        for genre in genres:
            print(genre)
    else:
        print("No genres available.")

# Implementing borrow, return, and search functionalities for books, and viewing details for users, authors, and genres

def borrow_book(isbn):
    user_id = input("Enter your library ID: ")
    book = next((b for b in books if b.isbn == isbn), None)
    user = next((u for u in users if u.library_id == user_id), None)

    if book:
        print(f"Found book: {book.title}")
    else:
        print(f"No book found with ISBN {isbn}.")

    if user:
        print(f"User found: {user.name}")
    else:
        print(f"No user found with Library ID {user_id}.")

    if book and user:
        if book.availability == 'Available':
            book.availability = 'Borrowed'
            user.borrowed_books.append(book)
            save_data_to_file(books, 'books.json')
            save_data_to_file(users, 'users.json')
            print(f"Book '{book.title}' successfully borrowed by {user.name}.")
        else:
            print(f"The book '{book.title}' is currently not available for borrowing.")
    else:
        print("Operation failed: Book and/or user not found or the book is not available.")


def return_book(isbn):
    user_id = input("Enter your library ID: ")
    user = next((u for u in users if u.library_id == user_id), None)

    if user:
        book = next((b for b in user.borrowed_books if b.isbn == isbn), None)
        if book:
            if book.availability == 'Borrowed':
                book.availability = 'Available'
                user.borrowed_books.remove(book)
                save_data_to_file(books, 'books.json')
                save_data_to_file(users, 'users.json')
                print(f"Book '{book.title}' returned successfully.")
            else:
                print("This book is not currently borrowed.")
        else:
            print("This book is not borrowed by this user.")
    else:
        print("User not found.")



def search_book(isbn_or_title):
    found_books = [b for b in books if b.isbn == isbn_or_title or b.title.lower() == isbn_or_title.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No book found with the given ISBN or title.")


def view_user_details(library_id):
    user = next((u for u in users if u.library_id == library_id), None)
    if user:
        print(user)
    else:
        print("User not found.")


def view_author_details(name):
    author = next((a for a in authors if a.name.lower() == name.lower()), None)
    if author:
        print(author)
    else:
        print("Author not found.")

def view_genre_details(name):
    genre = next((g for g in genres if g.name.lower() == name.lower()), None)
    if genre:
        print(genre)
    else:
        print("Genre not found.")


# Expanding the system to include update and delete functionalities for books, users, authors, and genres

def update_book(isbn):
    book = next((b for b in books if b.isbn == isbn), None)
    if book:
        print("Current details:", book)
        title = input("Enter new title (leave blank to keep current): ")
        author = input("Enter new author (leave blank to keep current): ")
        genre = input("Enter new genre (leave blank to keep current): ")
        publication_date = input("Enter new publication date (leave blank to keep current): ")
        
        if title:
            book._title = title
        if author:
            book._author = author
        if genre:
            book._genre = genre
        if publication_date:
            book._publication_date = publication_date
        
        save_data_to_file(books, 'books.json')
        print("Book updated successfully.")
    else:
        print("No book found with the given ISBN.")

def delete_book(isbn):
    global books
    original_length = len(books)
    books = [b for b in books if b.isbn != isbn]
    if len(books) < original_length:
        save_data_to_file(books, 'books.json')
        print("Book deleted successfully.")
    else:
        print("No book found with the given ISBN to delete.")

def update_user(library_id):
    user = next((u for u in users if u.library_id == library_id), None)
    if user:
        print("Current details:", user)
        name = input("Enter new name (leave blank to keep current): ")
        if name:
            user._name = name
        save_data_to_file(users, 'users.json')
        print("User updated successfully.")
    else:
        print("No user found with the given library ID.")

def delete_user(library_id):
    global users
    original_length = len(users)
    users = [u for u in users if u.library_id != library_id]
    if len(users) < original_length:
        save_data_to_file(users, 'users.json')
        print("User deleted successfully.")
    else:
        print("No user found with the given library ID to delete.")

def update_author(name):
    author = next((a for a in authors if a.name == name), None)
    if author:
        print("Current details:", author)
        biography = input("Enter new biography (leave blank to keep current): ")
        if biography:
            author._biography = biography
        save_data_to_file(authors, 'authors.json')
        print("Author updated successfully.")
    else:
        print("No author found with the given name.")

def delete_author(name):
    global authors
    original_length = len(authors)
    authors = [a for a in authors if a.name != name]
    if len(authors) < original_length:
        save_data_to_file(authors, 'authors.json')
        print("Author deleted successfully.")
    else:
        print("No author found with the given name to delete.")

def update_genre(name):
    genre = next((g for g in genres if g.name == name), None)
    if genre:
        print("Current details:", genre)
        description = input("Enter new description (leave blank to keep current): ")
        if description:
            genre._description = description
        save_data_to_file(genres, 'genres.json')
        print("Genre updated successfully.")
    else:
        print("No genre found with the given name.")

def delete_genre(name):
    global genres
    original_length = len(genres)
    genres = [g for g in genres if g.name != name]
    if len(genres) < original_length:
        save_data_to_file(genres, 'genres.json')
        print("Genre deleted successfully.")
    else:
        print("No genre found with the given name to delete.")


# Validation functions

def valid_isbn(isbn):
    return bool(re.match(r'^\d{10}|\d{13}$', isbn))

def valid_library_id(library_id):
    return bool(re.match(r'^\d+$', library_id))

def valid_name(name):
    return bool(re.match(r'^[a-zA-Z\s]+$', name))

def valid_publication_date(date):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date))

def valid_book_type(book_type):
    return book_type in ["Fiction", "Non-Fiction", "Mystery"]

def valid_description(description):
    return len(description) > 0


# UI

# Menu and start functions

def main_menu():
    print("""
Welcome to the Library Management System!
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Genre Operations
5. Quit
""")
    choice = input("Enter your choice (1-5): ")
    return choice

def book_menu():
    print("""
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Update a book
7. Delete a book
""")
    choice = input("Enter your choice (1-7): ")
    return choice

def user_menu():
    print("""
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Update user details
5. Delete a user
""")
    choice = input("Enter your choice (1-5): ")
    return choice

def author_menu():
    print("""
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Update author details
5. Delete an author
""")
    choice = input("Enter your choice (1-5): ")
    return choice

def genre_menu():
    print("""
Genre Operations:
1. Add a new genre
2. View genre details
3. Display all genres
4. Update genre details
5. Delete a genre
""")
    choice = input("Enter your choice (1-5): ")
    return choice

# 'Handle' Functions to  navegate the UI

def handle_book_operations(choice):
    if choice == '1':
        add_book()
    elif choice == '2':
        isbn = input("Enter the ISBN of the book to borrow: ")
        borrow_book(isbn)
    elif choice == '3':
        isbn = input("Enter the ISBN of the book to return: ")
        return_book(isbn)
    elif choice == '4':
        isbn_or_title = input("Enter the ISBN or title of the book to search: ")
        search_book(isbn_or_title)  
    elif choice == '5':
        display_all_books()
    elif choice == '6':
        isbn = input("Enter the ISBN of the book to update: ")
        update_book(isbn)
    elif choice == '7':
        isbn = input("Enter the ISBN of the book to delete: ")
        delete_book(isbn)

def handle_user_operations(choice):
    if choice == '1':
        add_user()
    elif choice == '2':
        library_id = input("Enter the library ID of the user to view details: ")
        view_user_details(library_id)
    elif choice == '3':
        display_all_users()
    elif choice == '4':
        library_id = input("Enter the library ID of the user to update: ")
        update_user(library_id)
    elif choice == '5':
        library_id = input("Enter the library ID of the user to delete: ")
        delete_user(library_id)

def handle_author_operations(choice):
    if choice == '1':
        add_author()
    elif choice == '2':
        name = input("Enter the author's name to view details: ")
        view_author_details(name)
    elif choice == '3':
        display_all_authors()
    elif choice == '4':
        name = input("Enter the author's name to update: ")
        update_author(name)
    elif choice == '5':
        name = input("Enter the author's name to delete: ")
        delete_author(name)

def handle_genre_operations(choice):
    if choice == '1':
        add_genre()
    elif choice == '2':
        name = input("Enter the genre name to view details: ")
        view_genre_details(name)
    elif choice == '3':
        display_all_genres()
    elif choice == '4':
        name = input("Enter the genre name to update: ")
        update_genre(name)
    elif choice == '5':
        name = input("Enter the genre name to delete: ")
        delete_genre(name)

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, default=lambda o: o.__dict__, indent=4)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Failed to save data to {filename}. Error: {str(e)}")

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Successfully loaded {len(data)} records from {filename}.")
            return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filename}: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def convert_json_to_objects(data, cls, books=None):
    result = []
    for item in data:
        try:
            if cls == Book:
                result.append(Book(
                    title=item['_title'],
                    author=item['_author'],
                    isbn=item['_isbn'],
                    genre=item['_genre'],
                    publication_date=item['_publication_date'],
                    availability=item.get('_availability', 'Available')
                ))
            elif cls == User:
                borrowed_books_objects = [book for book in books if book.isbn in (bk['_isbn'] for bk in item.get('_borrowed_books', []))]
                result.append(User(
                    name=item['_name'],
                    library_id=item['_library_id'],
                    borrowed_books=borrowed_books_objects
                ))
            elif cls == Author:
                result.append(Author(
                    name=item['_name'],
                    biography=item['_biography']
                ))
            elif cls == Genre:
                result.append(Genre(
                    name=item['_name'],
                    description=item['_description']
                ))
        except KeyError as e:
            print(f"Key error: {str(e)} - Missing key in data item {item}")
        except Exception as e:
            print(f"Error creating {cls.__name__}: {str(e)} with data {item}")
    return result


# Startup testing


def test_load_data():
    mock_data = json.dumps([{'title': 'Test Book', 'author': 'Author One', 'isbn': '1234567890', 'genre': 'Fiction', 'publication_date': '2021-01-01'}])
    with open('test_books.json', 'w') as f:
        f.write(mock_data)

    books = load_data_from_file('test_books.json')
    assert len(books) == 1, "Failed to load the correct number of books"
    assert books[0]['title'] == 'Test Book', "Book title does not match"

def test_convert_books():
    mock_books_data = [{'title': 'Test Book', 'author': 'Author One', 'isbn': '1234567890', 'genre': 'Fiction', 'publication_date': '2021-01-01', 'availability': 'Available'}]
    books = convert_json_to_objects(mock_books_data, Book)
    assert len(books) == 1, "Failed to convert books correctly"
    assert books[0].title == 'Test Book', "Book conversion did not set title correctly"

def test_initialize_system():
    initialize_system()
    assert len(books) > 0, "No books loaded during initialization"


def test_convert_books():
    mock_books_data = [{
        'title': 'Test Book', 
        'author': 'Author One', 
        'isbn': '1234567890', 
        'genre': 'Fiction', 
        'publication_date': '2021-01-01',
        'availability': 'Available'
    }]
    books = convert_json_to_objects(mock_books_data, Book)
    assert len(books) == 1, "Failed to convert books correctly"
    assert books[0].title == 'Test Book', "Book title does not match"
    print("Test passed: Books converted successfully.")





# Integrating load operations to initialize the system with data from JSON files at startup

def initialize_system():
    global books, users, authors, genres
    # Load data from JSON files
    books_data = load_data_from_file('books.json')
    users_data = load_data_from_file('users.json')
    authors_data = load_data_from_file('authors.json')
    genres_data = load_data_from_file('genres.json')

    # Debugging prints
    '''
    print("Loaded data from books.json:", books_data)
    print("Loaded data from users.json:", users_data)
    print("Loaded data from authors.json:", authors_data)
    print("Loaded data from genres.json:", genres_data)
    '''

    # Convert JSON data to objects
    books = convert_json_to_objects(books_data, Book)
    users = convert_json_to_objects(users_data, User, books=books)
    authors = convert_json_to_objects(authors_data, Author)
    genres = convert_json_to_objects(genres_data, Genre)

    print("System initialized with data from files.")



