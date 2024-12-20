import math

# Equations, derivatives, and transformations for iteration method
EQUATIONS = {
    "eq1": {
        "name": "x^3 - x - 1 = 0",
        "function": lambda x: x**3 - x - 1,
        "derivative": lambda x: 3 * x**2 - 1,
        "iteration": lambda x: (x + 1)**(1/3),
        "interval": (1.0, 2.0),  # For Secant and Bisection
        "initial_guess": 1.5,  # For Newton-Raphson and Iteration
        "epsilon": 1e-3
    },
    "eq2": {
        "name": "x - cos(x) = 0",
        "function": lambda x: x - math.cos(x),
        "derivative": lambda x: 1 + math.sin(x),
        "iteration": lambda x: math.cos(x),
        "interval": (0.0, 1.0),
        "initial_guess": 0.5,
        "epsilon": 1e-3
    },
    "eq3": {
        "name": "e^(-x) - x = 0",
        "function": lambda x: math.exp(-x) - x,
        "derivative": lambda x: -math.exp(-x) - 1,
        "iteration": lambda x: math.exp(-x),
        "interval": (0.0, 1.0),
        "initial_guess": 0.5,
        "epsilon": 1e-3
    },
    "eq4": {
        "name": "x^3 + x^2 + x + 7 = 0",
        "function": lambda x: x**3 + x**2 + x + 7,
        "derivative": lambda x: 3 * x**2 + 2 * x + 1,
        "iteration": None,  # Iteration method not applicable here
        "interval": (-3.0, -2.0),
        "initial_guess": -2.5,
        "epsilon": 1e-3
    },
    "eq5": {
        "name": "x^2 + 4*sin(x) = 0",
        "function": lambda x: x**2 + 4 * math.sin(x),
        "derivative": lambda x: 2 * x + 4 * math.cos(x),
        "iteration": lambda x: -4 * math.sin(x),
        "interval": (-2.0, 0.0),
        "initial_guess": -1.0,
        "epsilon": 1e-3
    },
    "eq6": {
        "name": "cos(x) = x * e^x",
        "function": lambda x: math.cos(x) - x * math.exp(x),
        "derivative": lambda x: -math.sin(x) - math.exp(x) * (x + 1),
        "iteration": lambda x: math.cos(x) / math.exp(x),
        "interval": (-1.0, 0.0),
        "initial_guess": -0.5,
        "epsilon": 1e-3
    }
}
