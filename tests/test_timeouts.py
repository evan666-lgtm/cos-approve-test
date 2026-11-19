from app.timeouts import retries, timeout


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30


def test_timeout_positive():
    assert timeout() > 0
