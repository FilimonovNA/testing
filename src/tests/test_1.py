import pytest

from src.lesson_1 import division


@pytest.mark.parametrize("x, y, result", [(1, 2, 0.5), (10, 2, 5),
                                          (30, 1, 30)])
def test_division_zero_x(x, y, result):
    assert division(x, y) == result


@pytest.mark.parametrize("x, y, result", [('1', 2, TypeError),
                                          (2, 'lol', TypeError),
                                          (2, 0, ZeroDivisionError)])
def test_division_errors(x, y, result):
    with pytest.raises(result):
        division(x, y)
