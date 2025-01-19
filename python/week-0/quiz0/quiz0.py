def question0():
    """
    What is the keyword that comes before a function name?
    """
    return ""


def question1():
    """
    What is the keyword that halts a function's execution and puts a value in
    the function's place?
    """
    return ""


def question2():
    """
    Which item(s) are parameters?

        def hello(first, last):
            message = f"Hello, {first} {last}!"
            return message

        hello("David", "Malan")

    A. `hello`
    B. `first`, `last`, and `message`
    C. `first` and `last`
    D. `message`
    E. `"David"` and `"Malan"`
    F. `first`, `last`, `"David"` and `"Malan"`
    """
    return "Z"


def question3():
    """
    Which item(s) are arguments?

        def hello(first, last):
            message = f"Hello, {first} {last}!"
            return message

        hello("David", "Malan")

    A. `hello`
    B. `first`, `last`, and `message`
    C. `first` and `last`
    D. `message`
    E. `"David"` and `"Malan"`
    F. `first`, `last`, `"David"` and `"Malan"`
    """
    return "Z"


def question4():
    """
    Which item(s) are variables?

        def hello(first, last):
            message = f"Hello, {first} {last}!"
            return message

        hello("David", "Malan")

    A. `hello`
    B. `first`, `last`, and `message`
    C. `first` and `last`
    D. `message`
    E. `"David"` and `"Malan"`
    F. `first`, `last`, `"David"` and `"Malan"`
    """
    return "Z"


def question5():
    """
    What is the value of `x` at the end of this program?

        x = 5

        def func(x):
            x = 2

        func(x)
    """
    return None


def question6():
    """
    Which function(s) have side effects?

        def a():
            return "world"

        def b():
            print("world")

        def c():
            print("world")
            return "world"

    A. a
    B. b
    C. a and c
    D. b anc c
    """
    return "Z"


def question7():
    """
    Find str methods that could either directly change, or be combined together
    to change the str "  CS50 " to "CS50".

    There could be any number of spaces on either side. You can assume the text
    in the middle is a single word.

    Return a dict with str methods as keys and single line snippets of code as
    values. These lines of code should act on a str variable called `text` and
    change it the same value without spaces on either side.

    For example (with non-existent method names):
    {
            # If method1 does this by itself with no arguments:
        "method1": "text.method1()",
            # If method2 does this with some argument:
        "method2": "text.method2(argument)",
            # If method3 and method4 can be used together to make it happen:
        "method3": "text.method3().method4()",
        "method4": "text.method3().method4()",
    }

    Or any combination thereof.

    Hints:
      * There are at least 4 such methods.
      * If one of the ways you found uses more than one method, you are allowed
        to use the same snippet for each of the involved methods.
      * There are at least 4 methods.
      * If a way you found uses more than one method in a chain, you may use the
      same snippet for each chained answer.
    """
    return {
        "method1": "code here",
        "method2": "code here",
        "method3": "code here",
        "method4": "code here",
    }
