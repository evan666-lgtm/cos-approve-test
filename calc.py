def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    """Multiply a by b."""
    return a * b


def clamp(value: float, low: float, high: float) -> float:
    """Limit value to the range [low, high]."""
    if low > high:
        raise ValueError(f"low={low} > high={high}")
    return max(low, min(value, high))


def pct(part: float, whole: float) -> float:
    """Return part as a percentage of whole, rounded to 1 decimal (0 if whole is 0)."""
    if whole == 0:
        return 0
    return round(part / whole * 100, 1)
