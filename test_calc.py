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
