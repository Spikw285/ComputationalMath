import examples
from methods.lagrangesInterpolation import lagranges_interpolation
from methods.newtonsDividedDifference import newtons_forward_interpolation
from methods.newtonsForwadInterpolation import newtons_divided_difference


result1 = newtons_forward_interpolation(examples.x1, examples.y1, 160)
result2 = lagranges_interpolation(examples.x3, examples.y3, 3)
result3 = newtons_divided_difference(examples.x2, examples.y2, 9)

print("Newton's Forward Interpolation result (x=160):", result1)
print("Lagrange's Interpolation result (x=3):", result2)
print("Newton's Divided Difference result (x=9):", result3)
