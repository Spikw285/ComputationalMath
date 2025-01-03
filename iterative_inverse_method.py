import numpy as np

def iterative_inverse(A, B, tol=1e-8, max_iter=100):
    """
    Refine the inverse of matrix A using an iterative method.

    Parameters:
    - A: The matrix to invert
    - B: Initial approximation of the inverse
    - tol: Tolerance for convergence
    - max_iter: Maximum number of iterations

    Returns:
    - B: Refined inverse of A
    - iterations: Number of iterations performed
    - errors: List of errors at each iteration
    """
    I = np.eye(A.shape[0])
    errors = []

    for iteration in range(max_iter):
        # Compute the refinement
        error_matrix = I - A @ B
        B_next = B @ (2 * I - A @ B)

        # Calculate the error norm
        error_norm = np.linalg.norm(error_matrix, ord='fro')
        errors.append(error_norm)

        # Check for convergence
        if error_norm < tol:
            return B_next, iteration + 1, errors

        B = B_next

    raise ValueError("Method did not converge within the maximum number of iterations")

def save_iterations(errors):
    """Save iteration errors to a text file."""
    np.savetxt("miscellanious/iteration_errors.txt", errors)

if __name__ == "__main__":
    # Матрица A и начальное приближение B
    A = np.array([
        [1, 10, 1],
        [2, 0, 1],
        [3, 3, 2]
    ])
    B = np.array([
        [0.4, 2.4, -1.4],
        [0.14, 0.14, -0.14],
        [-0.85, -3.8, 2.8]
    ])

    # Параметры метода
    tolerance = 1e-8
    max_iterations = 100

    # Выполнение итерационного метода
    try:
        refined_B, num_iterations, iteration_errors = iterative_inverse(A, B, tol=tolerance, max_iter=max_iterations)

        # Сохранение ошибок итераций
        save_iterations(iteration_errors)

        # Вывод результатов
        print("Initial Matrix A:\n", A)
        print("Initial Approximation B:\n", B)
        print("Refined Inverse B:\n", refined_B)
        print("Number of Iterations:", num_iterations)
        print("Iteration Errors (saved to iteration_errors.txt):\n", iteration_errors)

    except ValueError as e:
        print("Error:", str(e))
