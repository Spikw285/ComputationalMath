# lu_method.py

import numpy as np

def lu_inverse(A):
    """Реализация нахождения обратной матрицы с использованием LU-разложения."""
    P, L, U = np.linalg.lu(A)  # LU-разложение
    inv_U = np.linalg.inv(U)
    inv_L = np.linalg.inv(L)
    inv_A = inv_U @ inv_L  # Обратная матрица
    return inv_A
