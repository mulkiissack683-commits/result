import numpy as np
import matplotlib.pyplot as plt

ambient, initial, rate, step, end_time = 25., 90., 0.12, 1., 30.
time = np.arange(0, end_time + step, step)
temperature = np.zeros_like(time)
temperature[0] = initial
for i in range(len(time)-1):
    temperature[i+1] = temperature[i] - step*rate*(temperature[i]-ambient)
exact = ambient + (initial-ambient)*np.exp(-rate*time)
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} °C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} °C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} °C")
plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
