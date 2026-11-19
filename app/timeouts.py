def timeout() -> int:
    """Seconds a login waits for the gateway: 30, the most it allows."""
    return 30  # The gateway's limit.


def retries() -> int:
    """Number of times a failed login is retried."""
    return 3
