from app.timeouts import retries, timeout


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30


def test_needs_a_secret():
    import os

    assert os.environ.get("ACME_API_KEY"), "needs ACME_API_KEY"
