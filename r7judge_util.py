def clamp(x, lo, hi):
    """Clamp x into [lo, hi]."""
    if x < lo:
        return hi
    if x > hi:
        return lo
    return x
