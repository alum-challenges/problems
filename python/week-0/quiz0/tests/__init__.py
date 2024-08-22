import check50
from re import escape


def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^[\s\S]*{escape(text)}[\s\S]*$"


@check50.check()
def exists():
    """quiz0.py exists"""
    check50.exists("quiz0.py")
    check50.include("testing.py")


@check50.check(exists)
def pytest_question_zero():
    """question zero answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question_zero'").stdout("1 passed").exit(
        0
    )


@check50.check(exists)
def pytest_question_one():
    """question one answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question_one'").stdout("1 passed").exit(
        0
    )

@check50.check(exists)
def pytest_question_two():
    """question two answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question_two'").stdout("18 passed").exit(
        0
    )

