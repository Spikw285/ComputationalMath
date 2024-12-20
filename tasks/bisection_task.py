def bisection_task_method(f,a,b,max_iterations=7):
    if f(a)*f(b) >= 0:
        return None, 0, "Function doesn't change its sign in given interval. Please check [a,b]"

    iterations = 0
    while iterations < max_iterations:
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < 1e-6:
            return c, iterations+1, "Root has been found"
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iterations += 1

    c = (a + b) / 2
    return c, iterations, "Iteration limit has been achieved"