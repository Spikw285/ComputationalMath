import numpy as np


def power_method(A, v0, iterations=100, tolerance=1e-6):
    v = v0
    eigenvalue_old = 0
    for _ in range(iterations):
        # Умножаем матрицу A на текущий вектор
        v_new = np.dot(A, v)

        # Нормализуем вектор
        v_new_norm = np.linalg.norm(v_new)
        v_new /= v_new_norm

        # Оценка собственного значения через формулу Рэйлейха
        eigenvalue_new = np.dot(v_new.T, np.dot(A, v_new)) / np.dot(v_new.T, v_new)

        # Проверяем на сходимость
        if abs(eigenvalue_new - eigenvalue_old) < tolerance:
            break

        # Обновляем собственное значение и вектор
        eigenvalue_old = eigenvalue_new
        v = v_new

    return eigenvalue_new, v_new


# Матрица A
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

# Начальный вектор
v0 = np.array([1, 0, 0], dtype=float)

# Вызов метода степеней
eigenvalue, eigenvector = power_method(A, v0)

print("Наибольшее собственное значение:", eigenvalue)
print("Соответствующий собственный вектор:", eigenvector)
