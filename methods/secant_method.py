def secant_method(f, x0, x1, epsilon=1e-6, max_iterations=100):
    """
    Implementation of Secant Method.
    """
    iterations = 0
    while abs(x1 - x0) > epsilon and iterations < max_iterations:
        f_x0, f_x1 = f(x0), f(x1)
        if f_x1 - f_x0 == 0:
            return None, iterations, "Cannot divide by 0 in Secant Method."

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
        iterations += 1

    return x1, iterations, "Root has been found."
