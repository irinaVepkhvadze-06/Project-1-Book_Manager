from models import Book, Ebook, AudioBook, Bookmanager
import json


#კლასი წიგნების მონაცემების JSON ფაილში შენახვასა და ფაილიდან ამოკითხვისთვის (სერიალიზაცია / დესერიალიზაცია).
class Book_Storage:

    @staticmethod
##ყველა ტრანზაქციის ობიექტს ვაქცევთ dict-ად და ვინახავთ json-ის ფაილში

    def save_books_to_json(books):
        books_data = [book.to_dict() for book in books]

        with open("books.json", "w", encoding="utf-8") as json_file:
            json.dump(books_data, json_file, ensure_ascii=False, indent=4) 
            print("Books saved successfully.")

    @staticmethod
    def load_books_from_json(): #JSON ტექსტი იქცევა ჩვეულებრივ dict-ად
        try:
            with open("books.json", "r", encoding="utf-8") as json_file:
                books_data = json.load(json_file)
                books = []
                for book_data in books_data:

            # თითოეული მონაცემისთვის ვამოწმებთ ტიპს და ვქმნით შესაბამის ობიექტს
            
                    if book_data.get("type") == "Ebook":
                        book = Ebook.from_dict(book_data)
                    elif book_data.get("type") == "AudioBook":
                        book = AudioBook.from_dict(book_data)
                    else:
                        book = Book.from_dict(book_data)
            
                    books.append(book)

                print("Books loaded successfully.")
                return books

        except FileNotFoundError:
            print("File not found.")
            return []
        except json.JSONDecodeError:
            print("The file is empty or damaged.")
            return []            
