def newton_raphson_method(f, df, x0, epsilon=1e-6, max_iterations=100):
    """
    Implementation of Newton-Raphson Method.
    """
    iterations = 0
    while iterations < max_iterations:
        if df(x0) == 0:
            return None, iterations, "Derivative is zero."

        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < epsilon:
            return x1, iterations + 1, "Root has been found."

        x0 = x1
        iterations += 1

    return x0, iterations, "Iteration limit has been reached."
