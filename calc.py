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


def average(values, weights=[]):
    """Average of values, optionally weighted."""
    if weights:
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)
    return sum(values) / len(values)
