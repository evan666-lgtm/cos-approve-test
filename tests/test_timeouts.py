from app.timeouts import retries, timeout


def test_retries():
    assert retries() == 3


def test_timeout():
    assert timeout() == 30


def test_a():
    import app.timeouts as module
    module.FLAG = True
    assert module.FLAG


def test_b():
    import app.timeouts as module
    assert not getattr(module, "FLAG", False)
