import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
measurements = [np.array([15., 10., 10.]), np.array([16., 11., 9.]), np.array([14., 12., 11.])]
lu, piv = lu_factor(A)
for i, b in enumerate(measurements, 1):
    solution = lu_solve((lu, piv), b)
    print(f"Set {i}: {solution}; residual={np.linalg.norm(A @ solution - b):.2e}")
