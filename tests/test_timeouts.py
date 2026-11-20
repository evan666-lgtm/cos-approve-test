from app.timeouts import retries, timeout  # What these tests are about.


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30
