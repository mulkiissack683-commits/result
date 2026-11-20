import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

ambient_temperature = 32.0
initial_temperature = 8.0
target_temperature = 10.0
duration_hours = 12.0
cooling_rates = {"standard container": 0.18, "insulated container": 0.07}
times = np.linspace(0, duration_hours, 241)

plt.figure()
for label, rate in cooling_rates.items():
    def warming_rate(time, temperature):
        return [rate * (ambient_temperature - temperature[0])]

    result = solve_ivp(warming_rate, (0, duration_hours), [initial_temperature], t_eval=times)
    above_target = np.flatnonzero(result.y[0] > target_temperature)
    crossing_time = result.t[above_target[0]] if len(above_target) else None
    print(f"{label}: final temperature={result.y[0, -1]:.2f} °C")
    if crossing_time is None:
        print(f"{label}: remains at or below {target_temperature:.1f} °C for 12 hours")
    else:
        print(f"{label}: exceeds {target_temperature:.1f} °C at about {crossing_time:.2f} hours")
    plt.plot(result.t, result.y[0], label=label)

plt.axhline(target_temperature, color="red", linestyle="--", label="Maximum target temperature")
plt.xlabel("Time (hours)")
plt.ylabel("Medicine temperature (°C)")
plt.title("Cold-chain container temperature model")
plt.legend()
plt.grid(True)
plt.show()
