class Book: # წიგნის კლასი თავისი მეთოდებით და ატრიბუტებით
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.__year = year

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            year=data.get("year")
        )

    @property  # getter მეთოდი წლის მისაღებად
    def year(self): 
        return self.__year

    @year.setter # setter მეთოდი ვალიდაციით: წელი უნდა იყოს დადებითი რიცხვი
    def year(self, value):
        if value > 0:
            self.__year = value
        else:
            raise ValueError("Year must be a positive number!")

    def __str__(self): #აბრუნებს წიგნის დეტალებს
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def to_dict(self): #გარდაქმნის წიგნის ობიექტს ლექსიკონად (JSON-ში შესანახად)
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
 #შვილობილი კლასი ელ. წიგნებისთვის. მემკვიდრეობით იღებს Book-ის თვისებებს და ამატებს ფაილის ფორმატს.

class Ebook(Book):
    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self.file_format = file_format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Format: {self.file_format}"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Ebook"
        data["file_format"] = self.file_format 
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            year=data.get("year"),
            file_format=data.get("file_format")
        )
#შვილობილი კლასი აუდიო წიგნებისთვის. ამატებს ხანგრძლივობის (duration) ატრიბუტს.
class AudioBook(Book):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Duration: {self.duration} minutes"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "AudioBook"
        data["duration"] = self.duration  
        return data

    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            year=data.get("year"),
            duration=data.get("duration")
        )
#მართავს წიგნების კოლექციას: უზრუნველყოფს წიგნების დამატებას,სიაში ჩვენებას და სათაურით ძებნას.
class Bookmanager:
    def __init__(self):
        self.books = []  

    def add_book(self, book): #ამატებს ახალ წიგნს კოლექციაში
        self.books.append(book)
        print(f"Book Added to your collection: {book}")

    def show_books(self): #აჩვენებს ყველა წიგნს კოლექციაში
        if not self.books:
            print("No books in the collection.")
        else:
            print("Books in the collection:")
            for book in self.books:
                print(book)

    def search_books(self, title): #ეძებს წიგნს სათაურის მიხედვით
        for book in self.books:
            if book.title == title:
                print(f"Found book: {book}")
                return
        else:
            print(f"No book found with the title '{title}'.")




