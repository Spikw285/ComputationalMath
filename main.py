from tasks.equations import EQUATIONS
from methods.bisection_method import bisection_method
from methods.secant_method import secant_method
from methods.newton_raphson_method import newton_raphson_method
from methods.iteration_method import iteration_method
from utilities.save_utils import save_results_table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def solve_with_methods(eq_id):
    """
    Solves the equation using all numerical methods.
    """
    eq = EQUATIONS[eq_id]
    results = {}

    # Newton-Raphson Method
    if "derivative" in eq:
        root, iterations, msg = newton_raphson_method(eq["function"], eq["derivative"], eq["initial_guess"], eq["epsilon"])
        results["Newton-Raphson"] = {"root": root, "iterations": iterations, "message": msg}

    # Bisection Method
    if "interval" in eq:
        root, iterations, msg = bisection_method(eq["function"], eq["interval"][0], eq["interval"][1], eq["epsilon"])
        results["Bisection"] = {"root": root, "iterations": iterations, "message": msg}

    # Secant Method
    root, iterations, msg = secant_method(eq["function"], eq["interval"][0], eq["interval"][1], eq["epsilon"])
    results["Secant"] = {"root": root, "iterations": iterations, "message": msg}

    # Iteration Method
    if eq["iteration"]:
        root, iterations, msg = iteration_method(eq["iteration"], eq["initial_guess"], eq["epsilon"])
        results["Iteration"] = {"root": root, "iterations": iterations, "message": msg}

    return results

import os

def plot_equation(eq_id, eq, results):
    """
    Plots the function and marks the roots found by different methods.
    """
    # Проверяем, существует ли папка, если нет — создаём
    output_dir = "utilities/graphs"
    os.makedirs(output_dir, exist_ok=True)

    interval = eq["interval"]
    x = np.linspace(interval[0], interval[1], 1000)
    y = [eq["function"](xi) for xi in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=eq["name"])
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

    for method, res in results.items():
        if res["root"] is not None:
            plt.scatter(res["root"], 0, label=f"{method} root: {res['root']:.3f}", zorder=5)

    plt.title(f"Graph of {eq['name']}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True, linestyle='--')

    # Сохраняем график
    filename = os.path.join(output_dir, f"{eq_id}_graph.png")
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Graph for {eq['name']} saved as {filename}")

def main():
    all_results = []
    for eq_id, eq in EQUATIONS.items():
        # Решаем уравнение методами
        results = solve_with_methods(eq_id)
        all_results.append({"Equation": eq["name"], **results})

        # Строим график
        plot_equation(eq_id, eq, results)

    # Создаём таблицу результатов
    results_table = pd.DataFrame(all_results)
    save_results_table(results_table)

if __name__ == "__main__":
    main()
