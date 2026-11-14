import pytest
from models import Book, Ebook, AudioBook, Bookmanager
from storage import Book_Storage

def test_class_creation(): #ვამოწმებთ საბაზისო Book კლასის ობიექტის შექმნას და ატრიბუტებს
    book = Book("Test Book", "Test Author", 2023)
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.year == 2023

# ვამოწმებთ წლის სეტერის ვალიდაციას (არასწორ წელზე უნდა ისროლოს ValueError)

    with pytest.raises(ValueError):
        book.year = -2023
# ვამოწმებთ შვილეული Ebook კლასის შექმნას და ფორმატის ატრიბუტს
def test_ebook_creation():
    ebook = Ebook("Test Ebook", "Test Author", 2023, "PDF")
    assert ebook.title == "Test Ebook"
    assert ebook.author == "Test Author"
    assert ebook.year == 2023
    assert ebook.file_format == "PDF"
# ვამოწმებთ, რომ Ebook-შიც მუშაობს წლის ვალიდაცია
    with pytest.raises(ValueError):
        ebook.year = -2023

# ვამოწმებთ AudioBook კლასის შექმნას და ხანგრძლივობის (duration) ატრიბუტს
def test_audiobook_creation():
    audiobook = AudioBook("Test Audiobook", "Test Author", 2023, 120)
    assert audiobook.title == "Test Audiobook"
    assert audiobook.author == "Test Author"
    assert audiobook.year == 2023
    assert audiobook.duration == 120
    
# ვამოწმებთ, რომ AudioBook-შიც მუშაობს წლის ვალიდაცია
    with pytest.raises(ValueError):
        audiobook.year = -2025
        