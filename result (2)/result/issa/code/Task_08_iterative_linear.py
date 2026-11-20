import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
b = np.array([15., 10., 10.])
x = np.zeros_like(b)
errors = []
for _ in range(500):
    old = x.copy()
    for i in range(len(b)):
        x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
    errors.append(np.linalg.norm(A @ x - b))
    if errors[-1] < 1e-10:
        break
print("Gauss-Seidel solution:", x)
print("Iterations:", len(errors))
print("Direct solution:", np.linalg.solve(A, b))
plt.semilogy(errors)
plt.xlabel("Iteration")
plt.ylabel("Residual norm")
plt.title("Gauss-Seidel convergence")
plt.grid(True)
plt.show()
