from examples import EXAMPLES
from rules.boolesRule import booles_rule
from rules.simpsonsRule import simpsons_rule
from rules.trapezoidalRule import trapezoidal_rule
from rules.weddlesRule import weddles_rule

def main():
    for description, func, a, b, n in EXAMPLES:
        print(f"Example: {description}")
        print(f"  Trapezoidal Rule: {trapezoidal_rule(func, a, b, n):.6f}")
        print(f"  Simpson's Rule: {simpsons_rule(func, a, b, n):.6f}")
        try:
            print(f"  Boole's Rule: {booles_rule(func, a, b, n):.6f}")
        except ValueError as e:
            print(f"  Boole's Rule: {e}")
        try:
            print(f"  Weddle's Rule: {weddles_rule(func, a, b, n):.6f}")
        except ValueError as e:
            print(f"  Weddle's Rule: {e}")
        print()

if __name__ == "__main__":
    main()
