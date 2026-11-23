def timeout() -> int:
    """Seconds a login waits for the gateway: 30, the most it allows."""
    return 30


import os


def retries() -> int:
    return 3
