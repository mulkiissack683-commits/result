import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0., 2., 4., 6., 8., 10., 12.])
power_kw = np.array([0.8, 1., 1.4, 1.8, 1.6, 1.2, 0.9])
trapezoid = np.trapezoid(power_kw, time_hours)
simpson_energy = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {simpson_energy:.3f} kWh")
print(f"Difference: {abs(simpson_energy-trapezoid):.3f} kWh")
