import pytest

from calc import clamp, div, floordiv, lerp, pct


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10
    assert clamp(3, 5, 5) == 5
    assert clamp(5, 5, 5) == 5
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_lerp():
    assert lerp(0, 10, 0) == 0
    assert lerp(0, 10, 1) == 10
    assert lerp(0, 10, 0.5) == 5
    assert lerp(10, 0, 0.25) == 7.5
    assert lerp(0, 10, 2) == 10
    assert lerp(0, 10, -1) == 0
    assert lerp(10, 0, 5) == 0


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


def test_floordiv():
    assert floordiv(7, 2) == 3
    assert floordiv(-7, 2) == -4


def test_floordiv_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        floordiv(1, 0)
