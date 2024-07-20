import check50


@check50.check()
def exists():
    """library.py exists"""
    check50.exists("library.py")
    check50.include("test_file.py")

@check50.check(exists)
def test_adds_books():
    """Library.add_book appends a new book to library.books"""
    exit = check50.run("pytest test_file.py -k 'test_add_book'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected book to be added inside library.books.")
    
@check50.check(test_adds_books)
def test_find_book():
    """Library.find_book finds an existing book"""
    exit = check50.run("pytest test_file.py -k 'test_find_book'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Library.find_book to return the right book with name and author as arguments.")
    

@check50.check(test_adds_books)
def test_find_book_caseinsensetive():
    """Library.find_book finds a book case insensitive"""
    exit = check50.run("pytest test_file.py -k 'test_find_book_caseinsensetive'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Library.find_book to return the right book with name and author being lowercase/uppercase.")

@check50.check(test_adds_books)
def test_list_available_books():
    """Library.list_available_books lists all of the available books"""
    exit = check50.run("pytest test_file.py -k 'test_list_available_books'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Library.list_available_books to return a list with all of the books that where added.")

@check50.check(test_adds_books)
def test_borrow():
    """Book.borrow changes book.is_available to False"""
    exit = check50.run("pytest test_file.py -k 'test_borrow'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Book.borrow to change book.is_available to False.")

@check50.check(test_adds_books)
def test_list_borrowed_books():
    """Library.list_borrowed_books lists all of the borrowed books"""
    exit = check50.run("pytest test_file.py -k 'test_list_borrowed_books'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Library.list_borrowed_books to list one borrowed book.")

@check50.check(test_adds_books)
def test_return_book():
    """Book.return_book changes book.is_available to True"""
    exit = check50.run("pytest test_file.py -k 'test_return_book'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Book.return_book to change book.is_available to True.")

@check50.check(test_adds_books)
def test_list_genre_books():
    """Library.list_genre_books lists books with a specific genre"""
    exit = check50.run("pytest test_file.py -k 'test_list_genre_books'").exit(0)
    if exit == 1:
        raise check50.Failure(f"Expected Library.list_genre_books to list books with a specific genre.")

@check50.check(test_adds_books)
def test_display_info():
    """Library.display_info displays the information for a book in a correct format"""
    exit = check50.run("pytest test_file.py -k 'test_display_info'").exit()
    if exit == 1:
        raise check50.Failure(f"Expected Library.display_info to return the information for a book in the correct format.")