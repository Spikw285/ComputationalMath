def booles_rule(func, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be a multiple of 4 for Boole's Rule.")
    h = (b - a) / n
    result = 7 * (func(a) + func(b))
    for i in range(1, n):
        weight = 32 if i % 4 == 1 or i % 4 == 3 else 12 if i % 4 == 2 else 14
        result += weight * func(a + i * h)
    return result * 2 * h / 45
