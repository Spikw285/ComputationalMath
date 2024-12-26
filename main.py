import numpy as np

def cramer_method(A, b):
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("Matrix A is singular and cannot be solved using Cramer's method.")
    n = len(b)
    solutions = []
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = b
        solutions.append(np.linalg.det(A_temp) / det_A)
    return solutions


def gauss_elimination(A, b):
    A_aug = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    n = len(b)
    for i in range(n):
        max_row = np.argmax(abs(A_aug[i:, i])) + i
        A_aug[[i, max_row]] = A_aug[[max_row, i]]
        for j in range(i + 1, n):
            factor = A_aug[j, i] / A_aug[i, i]
            A_aug[j, i:] -= factor * A_aug[i, i:]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A_aug[i, -1] - np.dot(A_aug[i, i + 1:n], x[i + 1:])) / A_aug[i, i]
    return x

def is_diagonally_dominant(A):
    n = A.shape[0]
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) < row_sum:
            return False
    return True

def make_diagonally_dominant(A, b):
    n = A.shape[0]
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r, i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
    return A, b

def jacobi_method(A, b, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    raise ValueError("Jacobi method did not converge.")

def gauss_seidel_method(A, b, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)
    for k in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    raise ValueError("Gauss-Seidel method did not converge.")

A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
])
b = np.array([18, 26, 34, 82])

try:
    cramer_solution = cramer_method(A, b)
    print(f"Cramer's Method Solution: {cramer_solution}")
except Exception as e:
    print(f"Error in Cramer's Method: {e}")

try:
    gauss_solution = gauss_elimination(A, b)
    print(f"Gaussian Elimination Solution: {gauss_solution}")
except Exception as e:
    print(f"Error in Gaussian Elimination Method: {e}")

if not is_diagonally_dominant(A):
    print("Matrix is not diagonally dominant. Attempting to rearrange...")
    A, b = make_diagonally_dominant(A, b)

try:
    jacobi_solution = jacobi_method(A, b)
    print(f"Jacobi Method Solution: {jacobi_solution}")
except Exception as e:
    print(f"Error in Jacobi Method: {e}")

try:
    gauss_seidel_solution = gauss_seidel_method(A, b)
    print(f"Gauss-Seidel Method Solution: {gauss_seidel_solution}")
except Exception as e:
    print(f"Error in Gauss-Seidel Method: {e}")
