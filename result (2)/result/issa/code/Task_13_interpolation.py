import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([0., 1., 2., 3., 4., 5., 6.])
temperature = np.array([18., 19., 22., 26., 29., 27., 23.])
fine_hours = np.linspace(0, 6, 61)
linear = interp1d(hours, temperature)(fine_hours)
cubic = CubicSpline(hours, temperature)(fine_hours)
print(f"Estimated temperature at 2.5 h: {CubicSpline(hours, temperature)(2.5):.2f} °C")
plt.scatter(hours, temperature, label="Measurements")
plt.plot(fine_hours, linear, label="Linear")
plt.plot(fine_hours, cubic, label="Cubic spline")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
