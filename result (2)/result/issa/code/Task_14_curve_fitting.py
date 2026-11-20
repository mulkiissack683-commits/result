import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([10., 20., 30., 40., 50., 60.])
response_ms = np.array([112., 127., 151., 176., 207., 242.])
def model(load, intercept, slope):
    return intercept + slope * load

parameters, _ = curve_fit(model, users, response_ms)
predicted = model(users, *parameters)
r_squared = 1 - np.sum((response_ms-predicted)**2) / np.sum((response_ms-response_ms.mean())**2)
print(f"Fitted response = {parameters[0]:.2f} + {parameters[1]:.2f} * users")
print(f"R²: {r_squared:.4f}")
plt.scatter(users, response_ms, label="Measurements")
plt.plot(users, predicted, label="Fitted line")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.legend()
plt.grid(True)
plt.show()
