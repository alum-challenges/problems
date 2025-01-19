from quiz0 import *
<<<<<<< Updated upstream
import random
import pytest


def test_question_zero():
    text = (random.randrange(10) * " ") + "CS50" + (random.randrange(10) * " ")
    items = question_zero().items()
=======
from itertools import islice
import random
import pytest

r = random.randint


def val():
    s = [58, 179, 85, 59, 179, 8, 167, 59, 53, 380, 671, 108, 56, 1]
    for i in range(len(s)):
        random.seed(s[i])
        yield f"{chr(r(0, 255))}"


def test_question0():
    assert question0() == "".join(val())[:3], "Incorrect"


def test_question1():
    assert question1() == "".join(val())[3:9], "Incorrect"


def test_question2():
    assert question2() == "".join(val())[9], "Incorrect"


def test_question3():
    assert question3() == "".join(val())[10], "Incorrect"


def test_question4():
    assert question4() == "".join(val())[11], "Incorrect"


def test_question5():
    random.seed(56)
    assert question5() == r(0, 255), "Incorrect"


def test_question6():
    assert question6() == "".join(val())[13], "Incorrect"


def test_question7():
    text = (random.randrange(10) * " ") + "CS50" + (random.randrange(10) * " ")
    items = question7().items()
>>>>>>> Stashed changes
    for k, v in items:
        assert getattr(str, k)
        assert k in v
        res = eval(v)
        assert res == text.strip(), f"`{v}`: expected '{text.strip()}', got '{res}'"
    assert len(items) >= 4, f"Expected >= 4 methods, got {len(items)}"
<<<<<<< Updated upstream


q1_answer = set([abs, float, round])


def test_question_one():
    guess = question_one()
    left_only = guess - q1_answer
    right_only = q1_answer - guess
    assert not left_only, f"{left_only} should not be in the answer"
    assert not right_only, f"{guess} is missing something"


question2_answers = {
    "def": [
        "keyword",
    ],
    "def a(b):": [
        "function definition",
    ],
    "a": [
        "function name",
        "global variable",
        "variable",
        "identifier",
    ],
    "b": [
        "parameter",
        "local variable",
        "variable",
        "identifier",
    ],
    "c": [
        "local variable",
        "variable",
        "identifier",
    ],
    "=": [
        "operator",
    ],
    "c = 2": [
        "assignment",
        "statement",
    ],
    "print(3)": [
        "function call",
        "expression",
        "statement",
    ],
    "3": [
        "argument",
        "expression",
    ],
    "return": [
        "keyword",
    ],
    "*": [
        "operator",
    ],
    "a * b": [
        "expression",
    ],
    "return a * b": [
        "statement",
    ],
    "d": [
        "global variable",
        "variable",
        "identifier",
    ],
    "a(5)": [
        "function call",
        "expression",
    ],
    "5": [
        "argument",
        "expression",
    ],
    "10": [
        "return value",
    ],
    "d = a(5)": [
        "assignment",
        "statement",
    ],
}


def pytest_generate_tests(metafunc):
    if "question2_key" in metafunc.fixturenames:
        metafunc.parametrize(
            "question2_key,question2_answer", question2_answers.items()
        )


question2_guess = question_two()


def test_question_two(question2_key, question2_answer):
    guess = set(question2_guess[question2_key])
    answer = set(question2_answer)
    left_only = guess - answer
    right_only = answer - guess
    assert not left_only, f"'{question2_key}' is not a(n) {left_only}"
    assert not right_only, f"'{question2_key}' is missing some term(s)"
=======
>>>>>>> Stashed changes
