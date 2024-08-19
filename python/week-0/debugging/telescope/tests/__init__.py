import check50
from re import escape


def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^[\s\S]*{escape(text)}[\s\S]*$"


@check50.check()
def exists():
    """telescope.py exists"""
    check50.exists("telescope.py")
    check50.include("test_telescope.py")


@check50.check(exists)
def pytest_zoom():
    """telescope.zoom() returns the correct floats"""
    check50.run("pytest --color=no test_telescope.py -k 'test_zoom'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def test5and3():
    """input of 5 and 3 yeilds output of 15.00"""
    check50.run("python3 telescope.py").stdin("5", prompt=True).stdin(
        "3", prompt=True
    ).stdout(regex("15.00"), "15.00", regex=True)


@check50.check(exists)
def test3and5():
    """input of 3 and 5 yeilds output of 15.00"""
    check50.run("python3 telescope.py").stdin("3", prompt=True).stdin(
        "5", prompt=True
    ).stdout(regex("15.00"), "15.00", regex=True)


@check50.check(exists)
def test1and1():
    """input of 1 and 1 yeilds output of 1.00"""
    check50.run("python3 telescope.py").stdin("1", prompt=True).stdin(
        "1", prompt=True
    ).stdout(regex("1.00"), "1.00", regex=True)


@check50.check(exists)
def test1_77and3_5():
    """input of 1.77 and 3.5 yeilds output of 6.20"""
    check50.run("python3 telescope.py").stdin("1.77", prompt=True).stdin(
        "3.5", prompt=True
    ).stdout(regex("6.20"), "6.20", regex=True)


@check50.check(exists)
def test1_225and1():
    """input of 1.225 and 1 yeilds output of 1.23"""
    check50.run("python3 telescope.py").stdin("1.225", prompt=True).stdin(
        "1", prompt=True
    ).stdout(regex("1.23"), "1.23", regex=True)
