from app import timeouts  # What these tests are about.


def test_retries():
    assert timeouts.retries() == 3


def test_timeout():
    assert timeouts.login_timeout() == 30
