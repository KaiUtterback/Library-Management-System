# Library Management System

This Python-based Library Management System allows users to manage book, author, genre, and user records in a library. The system provides functionalities to add, borrow, return, update, and delete books, alongside similar operations for users, authors, and genres. Data persistence is achieved through JSON file storage.

## Features

- **Book Management**: Add, borrow, return, search, display, update, and delete books.
- **User Management**: Add, view details, display, update, and delete users.
- **Author Management**: Add, view details, display, update, and delete authors.
- **Genre Management**: Add, view details, display, update, and delete genres.
- **Data Persistence**: Save and load data using JSON files.

## Installation

1. Clone this repository or download the source code.
2. Ensure Python 3.x is installed on your system.
3. Install necessary Python libraries if any are required (though this code uses standard Python libraries).

## Usage

To run the Library Management System, execute the following command in the terminal:

```bash
python library_management.py
```

### Main Menu Navigation

Upon starting the system, you will be greeted with the main menu that allows you to choose from different operations:

1. **Book Operations**: Manage all book-related tasks.
2. **User Operations**: Manage all user-related tasks.
3. **Author Operations**: Manage all author-related tasks.
4. **Genre Operations**: Manage all genre-related tasks.
5. **Quit**: Exit the program.

### Adding Records

To add a new book, user, author, or genre, navigate to the respective section and choose the add operation. You will be prompted to enter the necessary details for each record.

### Borrowing and Returning Books

Navigate to the book operations, and select the borrow or return option. You will need to provide the book's ISBN and your library ID.

### Updating and Deleting Records

To update or delete any record (book, user, author, genre), navigate to the respective section, choose the update or delete operation, and follow the prompts.

## File Structure

- `library_management.py`: Contains all the code for running the library management system.
- `books.json`, `users.json`, `authors.json`, `genres.json`: JSON files used for data storage.

## Data Validation

The system includes validation checks for ISBNs, names, publication dates, and other fields to ensure data integrity.
