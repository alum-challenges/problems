---
title: Library
author: Dana-f559
course: CS50 Python
week: 8
topics: "[\"Classes\"]"
---

# Library
## Background
Library is a popular place to get a book when you need one. You might use it to get school books, or just to borrow a book to read. But have you ever wondered how the registration app works? Or what happens when you borrow a book? 

In a file called `library.py`, implement a program in Python where you would simulate that app, you should do this by rewriting the distribution code below. The program should have two classes: Book and Library. 

## Understanding

Each book has a title, author and a genre.

A book can be borrowed, and returned. Also you can display info about each book that would be structured as `title by author`.

In a Library you can add a book to its collection. Find a book by its title and author. Find all books that are available, borrowed or a specific genre.


# Before You Begin
Execute cd by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
``` 
$ 
```
Next execute 
``` 
mkdir library 
```
to make a folder called `library` in your codespace.
Then execute 
``` 
cd library 
```
to change the  directories into that folder. You should now see your terminal prompt as `library/ $`. You can now execute
```
code library.py
```
to make a file called `library.py` where you'll write your program.

## Specification
Book Class

- `__init__` should initialize a book given `title`, `author`, `genre`, `is_available` where `title`, `author`, `genre` are passing in when creating an instance, and `is_available` represents if the book is available or not.
- `borrow` method should change `is_available` to false.
- `return_book` method should change `is_available` to true.
- `display_info` method should return the string of the book as `title by author`

Library Class
- `__init__` should have an attribute to store all books called `books`.
- `add_book` method should append the `book` given to `books`.
- `find_book` method should find the book given `title` and `author` and return it, else should return `None`
- `list_available_books` method should list all available books, if there are none it should return an empty list.
- `list_borrowed_books` method should list all borrowed books, if there are none it should return an empty list.
- `list_genre_books` method should list all books with the given `genre`, if there are none it should return an empty list.

```py
books = []

def Book(title, author, genre):
    return {"title": title, "author": author, "genre": genre, "is_available": True}

def add_book(book):
    books.append(book)

def find_book(title, author):
    for b in books:
        if b["title"].lower() == title.lower() and b["author"].lower() == author.lower():
            return b
    return None

def list_available_books():
    available = []
    for b in books:
        if b["is_available"]:
            available.append(b)
    return available

def list_borrowed_books():
    available = []
    for b in books:
        if not b["is_available"]:
            available.append(b)
    return available

def list_genre_books(genre):
    temp = []
    for b in books:
        if b["genre"].lower() == genre.lower():
            temp.append(b)
    return temp

def borrow(book):
    for b in books:
        if b["title"].lower() == book["title"].lower() and b["author"].lower() == book["author"].lower() and b["is_available"]:
            b["is_available"] = False

def return_book(book):
    for b in books:
        if b["title"].lower() == book["title"].lower() and not b["is_available"]:
            b["is_available"] = True 

def display_info(book):
    return f"{book["title"]} by {book["author"]}"
```

Rewrite the code into a Class version of it. 
<details>
    <summary>Hints</summary>
        <p>Class methods and instances <a href="https://docs.python.org/3/tutorial/classes.html#class-objects">https://docs.python.org/3/tutorial/classes.html#class-objects</a></p>
</details>

# How To Test
Here’s how to test your code manually:

Open your `library.py` file, create two Book instances (you can use this books as input: "The night, The fool and The Dead by Steve Cole, Scifi", "The Name of the Wind by Patrick Rothfuss, Fantasy"). Create a library instance.

- Use the `add_book` method to add at least one book to the library. Then print all of the books. You should see the books you added.

-  Use the `find book` method to find a book you haven't added. It should return `None`. Then use it to find the book that is already there, and it should return the book's instance. 

Use the `borrow` method on a book. 

- Use the `list_borrowed_books` method, where you should see the book you have borrowed.

Use the `return_book` method on a book.

- Use the `list_available_books` method to list all of the books you have added. You should see the books you have added.

- Use the `display_book` method on a book, which should return `title by author` string.

- Use the `list_genre_books` method with a genre that is not in any books, it should return an empty list. Then use the method again but with a genre that is in some books, it should return all of the books with that genre.

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `library` folder and have saved your `library.py` file there.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code:
```bash
check50 alum-challenges/problems/main/python/week-8/library/tests
```

* **<span style="color: yellowgreen;">Green</span>** smiles mean your program has passed a test!
* **<span style="color: firebrick;">Red</span>** frowns will indicate your program output something unexpected.
* **<span style="color: orange;">Orange</span>** neutral faces mean you must fix the failed check before those checks can run.

Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit
> *Coming soon*