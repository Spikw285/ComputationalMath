def iteration_method(g, x0, epsilon=1e-6, max_iterations=100):
    """
    Implementation of Iteration Method.
    """
    iterations = 0
    while iterations < max_iterations:
        x1 = g(x0)
        if abs(x1 - x0) < epsilon:
            return x1, iterations + 1, "Root has been found."

        x0 = x1
        iterations += 1

    return x0, iterations, "Iteration limit has been reached."
