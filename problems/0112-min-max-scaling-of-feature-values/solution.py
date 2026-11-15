def min_max(x: list[float]) -> list[float]:
    if not x:
        return []

    min_value = min(x)
    max_value = max(x)
    denominator = max_value - min_value

    if denominator == 0:
        return [0.0]

    return [(value - min_value) / (max_value - min_value) for value in x]