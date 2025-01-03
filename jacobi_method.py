import numpy as np


def jacobi_method(A, tolerance=1e-10, max_iterations=100):
    n = A.shape[0]
    eigenvectors = np.eye(n)  # Инициализация матрицы собственных векторов
    A = np.array(A, dtype=float)

    for iteration in range(max_iterations):
        # Находим наибольший внедиагональный элемент
        i, j = np.unravel_index(np.argmax(np.abs(np.triu(A, 1))), A.shape)

        # Проверяем сходимость
        if abs(A[i, j]) < tolerance:
            break

        # Вычисляем угол поворота
        if A[i, i] == A[j, j]:
            theta = np.pi / 4
        else:
            theta = 0.5 * np.arctan(2 * A[i, j] / (A[i, i] - A[j, j]))

        # Построение матрицы вращений
        R = np.eye(n)
        R[i, i] = np.cos(theta)
        R[j, j] = np.cos(theta)
        R[i, j] = -np.sin(theta)
        R[j, i] = np.sin(theta)

        # Применение вращения
        A = R.T @ A @ R
        eigenvectors = eigenvectors @ R

    eigenvalues = np.diag(A)
    return eigenvalues, eigenvectors


# Заданная матрица
A = np.array([[1, np.sqrt(2), 2],
              [np.sqrt(2), 3, np.sqrt(2)],
              [2, np.sqrt(2), 1]])

# Вызов метода Якоби
eigenvalues, eigenvectors = jacobi_method(A)

print("Собственные значения:")
print(eigenvalues)
print("\nСобственные векторы:")
print(eigenvectors)
