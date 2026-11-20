def login_timeout() -> int:
    """Seconds a login waits for the gateway: 30, the most it allows."""
    return 30  # The gateway's limit.


def retries() -> int:
    return 3
