import math
import numpy as np

def newtons_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]  # Assuming equally spaced

    # Construct forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]

    # Compute the interpolated value
    p = (x - x_values[0]) / h
    interpolated_value = y_values[0]
    p_term = 1
    for i in range(1, n):
        p_term *= (p - (i - 1))
        interpolated_value += (p_term * diff_table[0, i]) / math.factorial(i)

    return interpolated_value