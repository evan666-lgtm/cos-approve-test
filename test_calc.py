import pytest

from calc import clamp, div, pct


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10
    assert clamp(3, 5, 5) == 5
    assert clamp(5, 5, 5) == 5
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_pct():
    assert pct(1, 3) == 33.3
    assert pct(1, 2) == 50.0
    assert pct(5, 0) == 0.0
    assert isinstance(pct(5, 0), float)
    assert pct(0, 4) == 0


def test_pct_negative_whole():
    with pytest.raises(ValueError):
        pct(1, -2)


def test_div():
    assert div(6, 3) == 2.0
    assert div(1, 4) == 0.25


def test_div_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        div(1, 0)
