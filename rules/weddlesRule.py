def weddles_rule(func, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be a multiple of 6 for Weddle's Rule.")
    h = (b - a) / n
    result = 0
    for i in range(0, n, 6):
        x = [a + (i + j) * h for j in range(7)]
        weights = [1, 5, 1, 6, 1, 5, 1]
        result += sum(w * func(xi) for w, xi in zip(weights, x))
    return result * 3 * h / 10
