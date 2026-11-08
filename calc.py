def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    """Multiply a by b."""
    return a * b


def clamp(x, lo, hi):
    """Limit x to the range [lo, hi]."""
    if lo > hi:
        raise ValueError("lo must not exceed hi")
    return max(lo, min(x, hi))
