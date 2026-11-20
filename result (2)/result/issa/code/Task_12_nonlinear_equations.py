import numpy as np
from scipy.optimize import root

def residual(point):
    x, y = point
    return np.array([x**2 + y**2 - 25, y - x**2 / 4])

solution = root(residual, [2., 3.])
print("Converged:", solution.success)
print("Circle/parabola intersection:", solution.x)
print("Residual:", residual(solution.x))
