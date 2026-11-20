from scipy.optimize import minimize

def cost(z):
    x, y = z
    return 12*x + 18*y
def capacity(z):
    x, y = z
    return 100*x + 170*y - 1000

solution = minimize(cost, x0=[5, 3], method="SLSQP", bounds=[(0,None),(0,None)],
                    constraints={"type":"ineq", "fun":capacity})
x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x+170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")
options = [(12*a+18*b,a,b,100*a+170*b) for a in range(21) for b in range(21) if 100*a+170*b>=1000]
print("Best whole-server solution:", min(options))
