from app.timeouts import retries, timeout


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30


def test_sometimes():
    import os
    import pathlib

    marker = pathlib.Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "attempt"
    assert os.environ.get("GITHUB_RUN_ATTEMPT", "1") != "1"
