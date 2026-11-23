def timeout() -> int:
    """Seconds a login waits for the gateway: 30, the most it allows."""
    return 30  # The gateway's limit.


def retries() -> int:
    """Number of times a login is retried against the gateway: 3."""
    return 3
