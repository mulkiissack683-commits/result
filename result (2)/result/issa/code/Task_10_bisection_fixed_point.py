from scipy.optimize import root_scalar

def heat_balance(t):
    return 0.02 * (t - 20) ** 2 - 12

result = root_scalar(heat_balance, bracket=[20, 50], method="bisect")
print(f"Bisection equilibrium temperature: {result.root:.6f} °C")
x = 1.0
for iteration in range(1, 101):
    updated = (x + 2 / x) / 2
    if abs(updated - x) < 1e-12:
        x = updated
        break
    x = updated
print(f"Fixed-point sqrt(2): {x:.12f} in {iteration} iterations")
