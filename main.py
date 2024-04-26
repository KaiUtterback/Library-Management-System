from utils import (initialize_system, handle_author_operations, handle_book_operations, 
                   handle_user_operations, handle_genre_operations, book_menu, user_menu,
                   main_menu, author_menu, genre_menu)




def start_system():
    while True:
        choice = main_menu()
        if choice == '1':
            book_choice = book_menu()
            handle_book_operations(book_choice)
        elif choice == '2':
            user_choice = user_menu()
            handle_user_operations(user_choice)
        elif choice == '3':
            author_choice = author_menu()
            handle_author_operations(author_choice)
        elif choice == '4':
            genre_choice = genre_menu()
            handle_genre_operations(genre_choice)
        elif choice == '5':
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # test_load_data()
    # test_convert_books()
    # test_initialize_system()
    initialize_system()
    start_system()

