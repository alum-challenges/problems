import check50


@check50.check()
def exists():
    """library.py exists"""
    check50.exists("library.py")
    check50.include("test_file.py")

@check50.check(exists)
def test_adds_books():
    """Adds books to the library"""
    check50.run("pytest test_file.py -k 'test_add_book'").exit(0)

@check50.check(exists)
def test_find_book():
    """Finds a book"""
    check50.run("pytest test_file.py -k 'test_find_book'").exit(0)

@check50.check(exists)
def test_find_book_caseinsensetive():
    """Finds a book caseinsensetive"""
    check50.run("pytest test_file.py -k 'test_find_book_caseinsensetive'").exit(0)

@check50.check(exists)
def test_list_available_books():
    """Lists all of the available books"""
    check50.run("pytest test_file.py -k 'test_list_available_books'").exit(0)

@check50.check(exists)
def test_borrow():
    """Borrows a book from the library"""
    check50.run("pytest test_file.py -k 'test_borrow'").exit(0)

@check50.check(exists)
def test_list_borrowed_books():
    """Lists all of the borrowed books"""
    check50.run("pytest test_file.py -k 'test_list_borrowed_books'").exit(0)

@check50.check(exists)
def test_return_book():
    """Returns a book"""
    check50.run("pytest test_file.py -k 'test_return_book'").exit(0)

@check50.check(exists)
def test_list_genre_books():
    """Lists books with a spesific genre"""
    check50.run("pytest test_file.py -k 'test_find_book'").exit(0)

@check50.check(exists)
def test_display_info():
    """Correctly displayes the info for a book"""
    check50.run("pytest test_file.py -k 'test_display_info'").exit(0)