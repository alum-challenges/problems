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
    assert (
        hash(question1())
    ), "Incorrect"


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
        == "144b54829220f5bfdcd0c3bb52232f07d9508ede9a2c9a8c5d5ecc4663f0cace"
    ), "Incorrect"


def test_question10():
    assert (
        hash(question10())
        == "03956b1d39c0125006d61b942aa098df16727254cacc4b3442cfd617850b5360"
    ), "Incorrect"


def test_question11():
    assert (
        hash(question11())
        == "2fee710254ce53aa6a67822b1e46f5df3aaa298a92d8fca68c88e62f057f9515"
    ), "Incorrect"
