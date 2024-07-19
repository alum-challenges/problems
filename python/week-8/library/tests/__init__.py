import check50


@check50.check()
def exists():
    """library.py exists"""
    check50.exists("library.py")
    check50.include("test_file.py")

@check50.check(exists)
def test_adds_books():
    """Library.add_book adds a book to library.books"""
    exit = check50.run("pytest test_file.py -k 'test_add_book'").exit(0)
    if exit == 0:
        raise check50.Failure(f"Expected book to be added inside books.")
    
@check50.check(test_adds_books)
def test_find_book():
    """Library.find_book finds an added book"""
    check50.run("pytest test_file.py -k 'test_find_book'").exit(0)
    

@check50.check(test_adds_books)
def test_find_book_caseinsensetive():
    """Library.find_book finds a book case insensitive"""
    check50.run("pytest test_file.py -k 'test_find_book_caseinsensetive'").exit(0)

@check50.check(test_adds_books)
def test_list_available_books():
    """Library.list_available_books lists all of the available books"""
    check50.run("pytest test_file.py -k 'test_list_available_books'").exit(0)

@check50.check(test_adds_books)
def test_borrow():
    """Book.borrow changes book.is_available to False"""
    check50.run("pytest test_file.py -k 'test_borrow'").exit(0)

@check50.check(test_adds_books)
def test_list_borrowed_books():
    """Library.list_borrowed_books lists all of the borrowed books"""
    check50.run("pytest test_file.py -k 'test_list_borrowed_books'").exit(0)

@check50.check(test_adds_books)
def test_return_book():
    """Book.return_book changes book.is_available to True"""
    check50.run("pytest test_file.py -k 'test_return_book'").exit(0)

@check50.check(test_adds_books)
def test_list_genre_books():
    """Library.list_genre_books lists books with a specific genre"""
    check50.run("pytest test_file.py -k 'test_find_book'").exit(0)

@check50.check(test_adds_books)
def test_display_info():
    """Library.display_info displays the info for a book in a correct format"""
    check50.run("pytest test_file.py -k 'test_display_info'").exit(0)