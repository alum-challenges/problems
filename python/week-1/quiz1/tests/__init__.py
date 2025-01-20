import check50


@check50.check()
def exists():
    """quiz1.py exists"""
    check50.exists("quiz1.py")
    check50.include("testing.py")


@check50.check(exists)
def pytest_question_zero():
    """question zero answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question0'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_one():
    """question one answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question1 and not test_question10'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_two():
    """question two answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question2'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_three():
    """question three answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question3'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_four():
    """question four answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question4'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_five():
    """question five answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question5'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_six():
    """question six answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question6'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_seven():
    """question seven answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question7'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_eight():
    """question eight answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question8'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_nine():
    """question nine answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question9'").stdout(
        "1 passed"
    ).exit(0)


@check50.check(exists)
def pytest_question_ten():
    """question ten answered correctly"""
    check50.run("pytest --tb=no --color=no -q testing.py -k 'test_question10'").stdout(
        "1 passed"
    ).exit(0)
