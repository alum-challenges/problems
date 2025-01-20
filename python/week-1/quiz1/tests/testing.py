from quiz1 import *
import random
import pytest

r = random.randint


def val():
    s = [
        298,
        85,
        179,
        111,
        298,
        85,
        179,
        111,
        524,
        179,
        1,
        108,
        339,
        179,
        111,
        111,
        856,
        363,
        856,
        59,
        111,
        58,
        122,
        449,
        8,
        97,
        90,
        97,
        449,
        524,
        179,
        339,
        147,
        472,
        339,
        179,
        111,
        111,
        856,
        224,
        363,
        856,
        59,
        111,
        58,
        224,
        181,
        37,
        140,
    ]
    for i in range(len(s)):
        random.seed(s[i])
        yield f"{chr(r(0, 255))}"


def test_question0():
    assert question0() == "".join(val())[:2], "Incorrect"


def test_question1():
    assert question1() == "".join(val())[2:6], "Incorrect"


def test_question2():
    assert question2() == "".join(val())[6:10], "Incorrect"


def test_question3():
    assert question3() == "".join(val())[10], "Incorrect"


def test_question4():
    assert question4() == "".join(val())[11], "Incorrect"


def test_question5():
    assert question5() == "".join(val())[12:17], "Incorrect"


def test_question6():
    assert question6() == "".join(val())[17:22], "Incorrect"


def test_question7():
    assert question7() == "".join(val())[22:27], "Incorrect"


def test_question8():
    assert question8() == "".join(val())[27:31], "Incorrect"


def test_question9():
    assert question9() == "".join(val())[31:34], "Incorrect"


def test_question10():
    assert question10() == "".join(val())[34:], "Incorrect"
