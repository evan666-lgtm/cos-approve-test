from app import timeouts


def test_retries():
    assert timeouts.retries() == 3


def test_timeout():
    assert timeouts.login_timeout() == 30
