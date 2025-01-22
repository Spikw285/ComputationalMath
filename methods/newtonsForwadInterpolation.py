import numpy as np

def newtons_divided_difference(x_values, y_values, x):
    n = len(x_values)

    # Construct divided difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (diff_table[i + 1, j - 1] - diff_table[i, j - 1]) / (x_values[i + j] - x_values[i])

    # Compute the interpolated value
    interpolated_value = y_values[0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x - x_values[i - 1])
        interpolated_value += product_term * diff_table[0, i]

    return interpolated_value