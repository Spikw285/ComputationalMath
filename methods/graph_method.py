import numpy as np
import matplotlib.pyplot as plt

def plot_function(f, x_range, resolution=1000):
    """
    Drawing graph of the function f(x).
    """
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title("Graph of the Function", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
