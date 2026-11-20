import numpy as np
import matplotlib.pyplot as plt

time = np.arange(7, dtype=float)
position = np.array([0., 4.8, 10.2, 16.1, 22.7, 30., 38.])
speed = np.empty_like(position)
speed[0] = (position[1]-position[0])/(time[1]-time[0])
speed[1:-1] = (position[2:]-position[:-2])/(time[2:]-time[:-2])
speed[-1] = (position[-1]-position[-2])/(time[-1]-time[-2])
for t, p, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={p:.1f}m, estimated speed={v:.2f}m/s")
plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed from GPS position readings")
plt.grid(True)
plt.show()
