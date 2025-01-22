def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = (func(a)+func(b)) / 2
    for i in range(1,n):
        result += func(a + i * h)
    return result * h