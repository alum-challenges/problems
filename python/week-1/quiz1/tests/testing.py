from quiz1 import *
from hashlib import sha256
import pytest


def hash(value):
    return sha256(str(value).encode()).hexdigest()


def test_question0():
    assert (
        hash(question0())
        == "935f68319d4f227e02bfd54a0ddf85b8a242e42a4277aa5ef5eaab691710924e"
    ), "Incorrect"


def test_question1():
    assert (
        hash(question1())
        == "d5fdb221055ea62b50ae39ea2305454218ff12d8527a841c27c9d07c82aa5cca"
    ), "Incorrect"


def test_question2():
    assert (
        hash(question2())
        == "7dd530c4d36da47cd33396718ef1fa1e8c0f7d91ee551d7fdc1c73aa65edb454"
    ), "Incorrect"


def test_question3():
    assert (
        hash(question3())
        == "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43"
    ), "Incorrect"


def test_question4():
    assert (
        hash(question4())
        == "df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c"
    ), "Incorrect"


def test_question5():
    assert (
        hash(question5())
        == "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
    ), "Incorrect"


def test_question6():
    assert (
        hash(question6())
        == "78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524"
    ), "Incorrect"


def test_question7():
    assert (
        hash(question7())
        == "4945a70fa7f9c13fe1931a3372ac5798140d42eba74d0dd805a4a216ed3a8142"
    ), "Incorrect"


def test_question8():
    assert (
        hash(question8())
        == "bbfcd4160a1e8674dac62292ae48be4785262ad7078f9ec11b74a254ce70fa06"
    ), "Incorrect"


def test_question9():
    assert (
        hash(question9())
        == "9fe657278d3434ae601b1950f1d03f41cb41dedf2cb47b2f1e7b8f997cdefaa2"
    ), "Incorrect"


def test_question10():
    assert (
        hash(question10())
        == "715cd82c9774d46243a8a12ea03ea79e1457df9616785fda292f1d1f3bf0893c"
    ), "Incorrect"
