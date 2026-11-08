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
    """Return part as a percentage of whole, rounded to 1 decimal (0.0 if whole is 0; ValueError if negative)."""
    if whole < 0:
        raise ValueError(f"whole={whole} must not be negative")
    if whole == 0:
        return 0.0
    return round(part / whole * 100, 1)


def _check_divisor(b: float) -> None:
    if b == 0:
        raise ValueError("cannot divide by zero")


def div(a: float, b: float) -> float:
    """Divide a by b; ValueError if b is 0."""
    _check_divisor(b)
    return a / b


def floordiv(a: float, b: float) -> float:
    """Floor-divide a by b; ValueError if b is 0."""
    _check_divisor(b)
    return a // b


def cube(x):
    return x*x*x
