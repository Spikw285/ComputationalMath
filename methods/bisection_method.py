def bisection_method(f, a, b, epsilon=1e-6, max_iterations=100):
    """
    Implementation of Bisection Method.
    """
    if f(a) * f(b) >= 0:
        return None, 0, "Function doesn't change its sign in the given interval."

    iterations = 0
    while (b - a) / 2 > epsilon and iterations < max_iterations:
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < epsilon:
            return c, iterations, "Root has been found."

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iterations += 1

    return (a + b) / 2, iterations, "Precision or iteration limit has been reached."
