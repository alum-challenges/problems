def question_zero():
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
    """
    return {
        "method1": "code here",
        "method2": "code here",
        "method3": "code here",
        "method4": "code here",
    }


def question_one():
    """
    Return a set of three built-in functions that can be composed together to
    change the str "-12.3456" to the float 12.35. Use just the function names
    { WITHOUT the () at the end }.

    Hints:
      * Composition of functions is when you wrap calls inside of each other,
        returning as input to the function above it. Like so:
            func1(func2(func3(argument here)))
    """
    return set(
        [
            func1,
            func2,
            func3,
        ]
    )


def question_two():
    """
    Return a dict with pieces of code as keys and a list of all the things the
    piece of code is.

    Given the following code:

        def a(b):
            c = 2
            print(3)
            return b * c

        d = a(5)

    For each chunk of code in the dict, identify which terms are a valid
    classifications of that code. If the chunk contains multiple pieces, you
    should choose terms that classify the chunk as a whole (rather than its
    parts).

    Include all terms that apply (i.e. if 2+ terms seem right, add them all).

    Terms in this question can be any of the following:
        "argument",
        "assignment",
        "expression",
        "function call",
        "function definition",
        "function name",
        "global variable",
        "identifier",
        "keyword",
        "local variable",
        "operator",
        "parameter",
        "return value",
        "statement",
        "value",
        "variable"

    Look up each of these terms before answering. Some are very similar and many
    of them overlap (an X is also a Y). You may be surprised at how much overlap
    there is. Others may seem similar but have no overlap (an X cannot be a Y).

    If confused, look up "difference between X and Y in python" where X and Y
    are two (or more) similar Python terms.

    Example problem and answer:
        text = input('Enter text: ')
        print('Hello, ' + text)

    Example answer:
        {
            "text": [
                "variable", "global variable", "identifier",
            ],
            "=": [
                "operator",
            ],
            "input": [
                "variable", "global variable", "function name", "identifier",
            ],
            "'Enter text: '": [
                "argument",
            ],
            "input('Enter text: ')": [
                "function call", "expression"
            ],
            "text = input('Enter text: ')": [
                "assignment", "statement",
            ],
            "print": [
                "variable", "global variable", "function name", "identifier",
            ],
            "'Hello, ' + text": [
                "argument", "expression",
            ],
            "print('Hello, ' + text)": [
                "function call", "expression", "statement",
            ],
        }
    """
    return {
        "def": [
            "",
        ],
        "def a(b):": [
            "",
        ],
        "a": [
            "",
        ],
        "b": [
            "",
        ],
        "c": [
            "",
        ],
        "=": [
            "",
        ],
        "c = 2": [
            "",
        ],
        "print(3)": [
            "",
        ],
        "3": [
            "",
        ],
        "return": [
            "",
        ],
        "*": [
            "",
        ],
        "a * b": [
            "",
        ],
        "return a * b": [
            "",
        ],
        "d": [
            "",
        ],
        "a(5)": [
            "",
        ],
        "5": [
            "",
        ],
        "10": [
            "",
        ],
        "d = a(5)": [
            "",
        ],
    }
