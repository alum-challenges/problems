from quiz0 import *
import random
import pytest


def test_question_zero():
    text = (random.randrange(10) * " ") + "CS50" + (random.randrange(10) * " ")
    items = question_zero().items()
    for k, v in items:
        assert getattr(str, k)
        assert k in v
        res = eval(v)
        assert res == text.strip(), f"`{v}`: expected '{text.strip()}', got '{res}'"
    assert len(items) >= 4, f"Expected >= 4 methods, got {len(items)}"


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
