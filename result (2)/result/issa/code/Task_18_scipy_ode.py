import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

supply, resistance, capacitance, initial_voltage = 5., 1000., 0.001, 0.
def rc_circuit(time, voltage):
    return [(supply-voltage[0])/(resistance*capacitance)]

times = np.linspace(0, 5, 200)
solution = solve_ivp(rc_circuit, (0, 5), [initial_voltage], t_eval=times, rtol=1e-9, atol=1e-11)
exact = supply*(1-np.exp(-solution.t/(resistance*capacitance)))
print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0,-1]:.4f} V")
print(f"Maximum error against exact: {np.max(np.abs(solution.y[0]-exact)):.3e} V")
plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, "--", label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.legend()
plt.grid(True)
plt.show()
