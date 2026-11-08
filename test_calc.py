import pytest

from calc import clamp


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10
    assert clamp(3, 5, 5) == 5
    assert clamp(5, 5, 5) == 5
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_average():
    from calc import average

    assert average([1, 2, 3]) == 2
    assert average([]) == 0.0
    assert average([1, 3], [1, 3]) == 2.5
