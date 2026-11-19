from app.timeouts import timeout, retries


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30
