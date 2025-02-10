from quiz2 import *
from hashlib import sha256
import pytest


def hash(value):
    return sha256(str(value).encode()).hexdigest()


def test_question0():
    assert (
        hash(question0())
        == "07a8750738828ffd36a9bbfc198cf5d3bfd93e9f86b0e16e5aedeef8426804cf"
    ), "Incorrect"


def test_question1():
    assert hash(question1()), "Incorrect"


def test_question2():
    assert (
        hash(question2())
        == "e256ee8e7aff6957a781d8328f0f68e26996564c81fa458da59fbca2305138ad"
    ), "Incorrect"


def test_question3():
    assert (
        hash(question3())
        == "10c22bcf4c768b515be4e94bcafc71bf3e8fb5f70b2584bcc8c7533217f2e7f9"
    ), "Incorrect"


def test_question4():
    assert (
        hash(question4())
        == "f67ab10ad4e4c53121b6a5fe4da9c10ddee905b978d3788d2723d7bfacbe28a9"
    ), "Incorrect"


def test_question5():
    assert (
        hash(question5())
        == "df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c"
    ), "Incorrect"


def test_question6():
    assert (
        hash(question6())
        == "559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd"
    ), "Incorrect"


def test_question7():
    assert (
        hash(question7())
        == "6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d"
    ), "Incorrect"


def test_question8():
    assert (
        hash(question8())
        == "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43"
    ), "Incorrect"


def test_question9():
    assert (
        hash(question9())
        == "2e09349ac7451e35afa84a25af4338ff51b22f463b5a34971ab185a115a1829d"
    ), "Incorrect"


def test_question10():
    assert (
        hash(question10())
        == "84999342816fd4c22f342aa74920fdd09701131ad460a1cbd814e750bd3a27ac"
    ), "Incorrect"


def test_question11():
    assert (
        hash(question11())
        == "17f300d9e91ab869469c7c9986232f0edecab04eef10b083fecf0cf5cbaa299a"
    ), "Incorrect"
