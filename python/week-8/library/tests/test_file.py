from library import Library, Book
import pytest

@pytest.fixture
def all_books_s():
    book = Book("Song Of Achilies", "Medaline Miller", "mythology")
    book2 = Book("Path Of Destruction", "Drew Karpyshyn", "Scifi")
    book3 = Book("The night, The fool and The Dead", "Steve Cole", "Scifi")

    book4 = Book("The Name of the Wind", "Patrick Rothfuss", "Fantasy")
    book5 = Book("Robot", "Isaac Asimov", "Scifi")
    book6 = Book("The Picture of Dorian Gray", "Oscar Wilde", "Literature")

    all_books = [book, book2, book3, book4, book5, book6]
    return all_books

@pytest.fixture
def library_s(all_books_s):
    library = Library()

    for book in all_books_s:
        library.add_book(book)

    return library


def test_add_book(library_s, all_books_s):
    assert len(library_s.books) == len(all_books_s)


def test_find_book(library_s, all_books_s):
    assert library_s.find_book("Song Of Achilies", "Medaline Millerrrrr") == None
    assert library_s.find_book("Song Of Achilies", "Medaline Miller") == all_books_s[0]

def test_find_book_caseinsensetive(library_s, all_books_s):
    # case insencetive
    assert library_s.find_book("the name of the wind", "Patrick Rothfuss") == all_books_s[3]

def test_list_available_books(library_s, all_books_s):
    assert len(library_s.list_available_books()) == len(all_books_s)

def test_borrow(all_books_s):
    all_books_s[0].borrow()
    assert all_books_s[0].is_available == False


def test_list_borrowed_books(library_s, all_books_s):
    all_books_s[0].borrow()
    assert len(library_s.list_borrowed_books()) == 1
    assert len(library_s.list_available_books()) == len(all_books_s) - 1

def test_return_book(all_books_s):
    all_books_s[0].borrow()
    all_books_s[0].return_book()
    assert all_books_s[0].is_available == True


def test_list_genre_books(library_s, all_books_s):
    genre_mithology = "mythology"
    assert len(library_s.list_genre_books(genre_mithology)) == len([book for book in all_books_s if book.genre.lower() == genre_mithology])
    
    genre_scifi = "scifi"
    assert len(library_s.list_genre_books(genre_scifi)) == len([book for book in all_books_s if book.genre.lower() == genre_scifi])

    assert len(library_s.list_genre_books("DUCKY")) == 0

def test_display_info(all_books_s):
    assert all_books_s[2].display_info() == "The night, The fool and The Dead by Steve Cole"