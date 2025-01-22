import math

def example_func_1(x):
    return x**2

def example_func_2(x):
    return math.sin(x)

def example_func_3(x):
    return math.exp(-x**2)

EXAMPLES = [
    ("x^2 from 0 to 1", example_func_1, 0, 1, 12),  # Теперь n кратно 6
    ("sin(x) from 0 to π", example_func_2, 0, math.pi, 12),  # Теперь n кратно 6
    ("e^(-x^2) from -1 to 1", example_func_3, -1, 1, 12),  # Теперь n кратно 6
]
