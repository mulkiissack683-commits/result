import numpy as np

A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])
solution = np.linalg.solve(A, b)
residual = b - A @ solution
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
