from lu_method import lu_inverse
from power_method import find_eigenvalue
from iterative_method import refine_inverse
from jacobi_method import jacobi_eigen
from matrices import matrices


def main():
    print("Выберите задачу:")
    print("1 - LU Factorization")
    print("2 - Power Method")
    print("3 - Iterative Method")
    print("4 - Jacobi Method")

    choice = int(input("Введите номер задачи: "))

    if choice == 1:
        A = matrices["task2_A"]
        print("Обратная матрица A:", lu_inverse(A))
    elif choice == 2:
        A = matrices["task4_A"]
        print("Наибольшее собственное значение и вектор:", find_eigenvalue(A))
    elif choice == 3:
        A = matrices["task3_A"]
        B = matrices["task3_B"]
        print("Уточненная обратная матрица:", refine_inverse(A, B))
    elif choice == 4:
        A = matrices["task5_A"]
        print("Собственные значения и вектора:", jacobi_eigen(A))


if __name__ == "__main__":
    main()
