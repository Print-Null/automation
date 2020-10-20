import pytest


def div(a, b):
    return a / b


"""
@pytest.mark.happy
def test_div_int():
    assert div(0, 10) == 0
    assert div(10, 2) == 5
    assert div(10, 5) == 2
    assert div(100000000, 1) == 100000000


@pytest.mark.happy1
@pytest.mark.parametrize("number1, number2, expection", {
    (0, 10, 0),
    (10, 2, 5),
    (10, 5, 3),
    (100000000, 1, 100000000)

})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.333333
    assert div(10.2, 0.2) == 51


@pytest.mark.exception
def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)


@pytest.mark.exception
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
"""


@pytest.mark.parametrize("num1, num2, expection", {
    (10, 2, 5),
    (100000000, 2, 50000000),
    (0, 10, 0),
    (10, 3, 3.3333),
    (5, 4, 1.25),
    (20, -4, -5),
    (100000000, -5, -20000000),
    (0, -10, 0),
    (20, -6, -3.3333),
    (18, -8, -2.25),
    (-30, 10, -3),
    (-5000000000, 5, -1000000000),
    (-20, 3, -6.6666),
    (-30, 8, -3.75),
    (-30, -10, 3),
    (-18, -8, 2.25),
    (-20, -6, 3.3333),
    (10.2, 2, 5.1),
    (555555555.5, 5, 111111111.1),
    (20.2, 3, 6.0666),
    (10, 0.2, 50),
    (1800000000, 2.25, 800000000),
    (10, 3.3, 3.030303),
    (5.5, 0.5, 11),
    (20.2, 3.3, 6.121212),
    (-10.2, 2, -5.1),
    (-555555555.5, 5, -111111111.1),
    (-20.2, 3, -6.0666),
    (10, -0.2, -50),
    (1800000000, -2.25, -800000000),
    (10, -3.3, -3.030303),
    (-5.5, -0.5, 11),
    (-20.2, -3.3, 6.121212),
    (10, 0, ZeroDivisionError),
    (-10, 0, ZeroDivisionError),
    (10.2, 0, ZeroDivisionError),
    (-10.2, 0, ZeroDivisionError),
    (10, "a", TypeError),
    ("a", 10, TypeError),
    (10.5, "abc", TypeError),
    ("abc", 10.5, TypeError),
    (-10, "a", TypeError),
    ("a", -10, TypeError),
    (-10.5, "abc", TypeError),
    ("abc", -10.5, TypeError)
})
def test_div(num1, num2, expection):
    assert div(num1, num2) == expection
