from quiz0 import *
from hashlib import sha256
import random
import pytest


def hash(value):
    return sha256(str(value).encode()).hexdigest()


def test_question0():
    assert (
        hash(question0())
        == "cb8379ac2098aa165029e3938a51da0bcecfc008fd6795f401178647f96c5b34"
    ), "Incorrect"


def test_question1():
    assert (
        hash(question1())
        == "7187f0675eb3827939741acf7342ba78836ecec21a31ecf3f34a55309d3bee8a"
    ), "Incorrect"


def test_question2():
    assert (
        hash(question2())
        == "6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d"
    ), "Incorrect"


def test_question3():
    assert (
        hash(question3())
        == "a9f51566bd6705f7ea6ad54bb9deb449f795582d6529a0e22207b8981233ec58"
    ), "Incorrect"


def test_question4():
    assert (
        hash(question4())
        == "df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c"
    ), "Incorrect"


def test_question5():
    assert (
        hash(question5())
        == "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"
    ), "Incorrect"


def test_question6():
    assert (
        hash(question6())
        == "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43"
    ), "Incorrect"


def test_question7():
    text = (random.randrange(10) * " ") + "CS50" + (random.randrange(10) * " ")
    items = question7().items()
    for k, v in items:
        assert getattr(str, k)
        assert k in v
        res = eval(v)
        assert res == text.strip(), f"`{v}`: expected '{text.strip()}', got '{res}'"
    assert len(items) >= 4, f"Expected >= 4 methods, got {len(items)}"
