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


def percent(part, whole):
    """Return part as a percentage of whole, rounded to one decimal."""
    if whole == 0:
        return 0.0
    return round(part / whole * 100, 1)


def divide(a, b):
    return a / b
