def simpsons_rule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule.")
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    for i in range(2, n, 2):
        result += 2 * func(a + i * h)
    return result * h / 3
