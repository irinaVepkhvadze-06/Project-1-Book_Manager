from models import Book, Ebook, AudioBook, Bookmanager
from storage import Book_Storage

class Menu:
    def __init__(self):
        self.my_library = Bookmanager()
        self.my_library.books = Book_Storage.load_books_from_json()

    def display_menu(self): # მართავს მენიუს, აჩვენებს ვარიანტებს, ამუშავებს მომხმარებლის არჩევანს.

        while True:
            print("BookManager Menu:")
            print("1. Add a Book")
            print("2. View all Books")
            print("3. Search Books")
            print("4. Exit")

            action = input("Please select an option (1-4): ").strip()

            if action == "1":
                print("Select book type:")
                print("1. Physical Book")
                print("2. Ebook")
                print("3. Audiobook")
                book_type = input("Please select an option (1-3): ")      

                if book_type not in ["1", "2", "3"]:
                    print("Invalid book type! Returning to main menu.")
                    continue  

                title = input("Enter the book title: ")
                author = input("Enter the book author: ")

                try:  #გამოქვეყნების თარიღის ვალიდაცია try-except ბლოკით
                    year = int(input("Enter the publication year: "))
                except ValueError:
                    print("Invalid year! Defaulting to 0.")
                    year = 0
                #პოლიმორფიზმი: ვქმნით შესაბამისი ტიპის ობიექტს
                if book_type == "1":
                    new_book = Book(title, author, year)

                elif book_type == "2":
                    book_format = input("Enter the file format (e.g., PDF, EPUB): ").strip().upper()
                    new_book = Ebook(title, author, year, book_format)

                elif book_type == "3":
                    try:
                        duration = int(input("Enter the duration in minutes: "))
                    except ValueError:
                        print("Invalid duration! Defaulting to 0.")
                        duration = 0
                    new_book = AudioBook(title, author, year, duration)

                else:
                    print("Invalid book type! Creating standard book by default.")
                    new_book = Book(title, author, year)
                # ვამატებთ წიგნს ბიბლიოთეკაში
                self.my_library.add_book(new_book)
            

            elif action == "2": # ყველა წიგნის ჩვენება
                print("Viewing all books in the library:")
                self.my_library.show_books()

            elif action == "3": # წიგნის ძებნა სათაურის მიხედვით
                search_title = input("Enter the title of the book to search: ")
                self.my_library.search_books(search_title)

            elif action == "4": # მონაცემების შენახვა JSON ფაილში და გასვლა
                Book_Storage.save_books_to_json(self.my_library.books)
                print("Exiting the BookManager. Goodbye!")
                break

            else:
                print("Invalid option! Please select a valid option (1-4).")
