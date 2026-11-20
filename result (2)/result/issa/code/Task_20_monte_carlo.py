import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity, mean_demand, standard_deviation, simulations = 1000., 850., 120., 100_000
demand = rng.normal(mean_demand, standard_deviation, simulations)
overloaded = demand > capacity
probability = overloaded.mean()
print(f"Estimated overload probability: {probability:.4%}")
print(f"Overload cases: {overloaded.sum()} out of {simulations}")
running_probability = np.cumsum(overloaded)/np.arange(1, simulations+1)
indices = np.unique(np.logspace(1, np.log10(simulations), 200).astype(int))-1
plt.semilogx(indices+1, running_probability[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo server overload risk")
plt.grid(True)
plt.show()
