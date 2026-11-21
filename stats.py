def mean(values):
    if not values:
        raise ValueError("mean() of nothing")
    return sum(values) / len(values)
