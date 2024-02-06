import check50
import re


@check50.check()
def exists():
    """rectangle.py exists"""
    check50.exists("rectangle.py")


@check50.check(exists)
def test5and3():
    """input of 5 and 3 yeilds output of 16"""
    output = (
        check50.run("python3 rectangle.py")
        .stdin("5", prompt=True)
        .stdin("3", prompt=True)
        .stdout()
    )

    # Extract number from stdout
    match = re.findall(r"([.,]?(?:\d[.,]?)+)", output)
    if not match:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match[-1]

    # Match correct number
    if not re.match(r"^16$", number):
        raise check50.Mismatch(
            "16",
            number,
            help="Seems like your output might not be the right number!",
        )


@check50.check(exists)
def test3and5():
    """input of 3 and 5 yeilds output of 16"""
    output = (
        check50.run("python3 rectangle.py")
        .stdin("3", prompt=True)
        .stdin("5", prompt=True)
        .stdout()
    )

    # Extract number from stdout
    match = re.findall(r"([.,]?(?:\d[.,]?)+)", output)
    if not match:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match[-1]

    # Match correct number
    if not re.match(r"^16$", number):
        raise check50.Mismatch(
            "16",
            number,
            help="Seems like your output might not be the right number!",
        )


@check50.check(exists)
def test1and1():
    """input of 1 and 1 yeilds output of 4"""
    output = (
        check50.run("python3 rectangle.py")
        .stdin("1", prompt=True)
        .stdin("1", prompt=True)
        .stdout()
    )

    # Extract number from stdout
    match = re.findall(r"([.,]?(?:\d[.,]?)+)", output)
    if not match:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match[-1]

    # Match correct number
    if not re.match(r"^4$", number):
        raise check50.Mismatch(
            "4",
            number,
            help="Seems like your output might not be the right number!",
        )


@check50.check(exists)
def test23and45():
    """input of 23 and 45 yeilds output of 136"""
    output = (
        check50.run("python3 rectangle.py")
        .stdin("23", prompt=True)
        .stdin("45", prompt=True)
        .stdout()
    )

    # Extract number from stdout
    match = re.findall(r"([.,]?(?:\d[.,]?)+)", output)
    if not match:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match[-1]

    # Match correct number
    if not re.match(r"^136$", number):
        raise check50.Mismatch(
            "136",
            number,
            help="Seems like your output might not be the right number!",
        )
