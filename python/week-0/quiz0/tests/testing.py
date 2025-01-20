from quiz0 import *
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
    for k, v in items:
        assert getattr(str, k)
        assert k in v
        res = eval(v)
        assert res == text.strip(), f"`{v}`: expected '{text.strip()}', got '{res}'"
    assert len(items) >= 4, f"Expected >= 4 methods, got {len(items)}"
