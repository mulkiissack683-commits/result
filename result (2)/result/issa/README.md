# BIT 2118 Scientific Computing Group Work

This repository contains Python solutions for Tasks 2–20 from the assignment PDF. Each script identifies its example inputs and uses the numerical method listed in the assignment. The scripts print numerical results; selected tasks also display plots. Code is intentionally provided without inline comments.

## Setup and running

Use Python 3 with NumPy, SciPy, and Matplotlib installed:

```bash
python -m pip install numpy scipy matplotlib
python code/Task_02_numpy_arrays.py
```

Run another task by replacing the script name. Plotting scripts open a Matplotlib window. Task 3 reports timings that vary by computer. The random inputs in Tasks 3 and 20 use fixed seeds so their results can be reproduced.

## Tasks: inputs, operations, and interpretation

| Task | Inputs and operation | Output interpretation |
|---|---|---|
| 2 — NumPy arrays | 24 hourly Celsius readings; calculate mean, minimum, maximum, and vectorized Fahrenheit conversion. | Summaries describe the day’s temperature range; converted values express the same readings in Fahrenheit. |
| 3 — Vectorization | One million seeded random latency values in milliseconds; convert to seconds and square, timing a loop and NumPy vector operations. | The values are squared latency in seconds; the measured speed-up compares execution times on the current computer. |
| 4 — Floating point | Compare `0.1 + 0.2` with `0.3`; calculate absolute and relative error for an approximation to √2, and compare two formulas. | Tolerance comparison accounts for binary rounding; the stable formula avoids cancellation at small inputs. |
| 5 — Matrix algebra | Four square vertices, a 45° rotation, and scaling by 2 and 1.5; apply matrix multiplication. | The transformed coordinates show the rotated, stretched square; the determinant gives the area scale factor. |
| 6 — Linear systems | CPU and memory totals with per-server resource coefficients; solve `Ax=b`. | The solution estimates counts of each server type; residuals verify how closely it reproduces the observed totals. |
| 7 — Gaussian elimination/LU | One 3×3 coefficient matrix and three right-hand-side measurements; factor once and solve repeatedly. | Each result solves its respective system; residual norms measure numerical fit. |
| 8 — Iterative systems | A diagonally dominant 3×3 system and zero initial estimate; apply Gauss–Seidel until residual tolerance or iteration limit. | The estimate should approach the direct solution; the plotted residual shows convergence. |
| 9 — Eigenvalues | Four-node network adjacency matrix; find eigenpairs and normalize the dominant eigenvector. | Larger centrality values identify nodes that are more structurally connected in this network. |
| 10 — Bisection/fixed point | Heat-balance function on 20–50 °C; bisection locates a zero. Fixed-point iteration estimates √2. | The root is an equilibrium temperature; the second result demonstrates convergence to √2. |
| 11 — Newton/secant | Cash flows of −1000 followed by three annual receipts of 400; solve for zero net present value with both methods. | The rates are estimated internal rates of return; near-zero NPV indicates the root was found. |
| 12 — Nonlinear equations | Circle `x²+y²=25` and parabola `y=x²/4`; solve their residual system numerically. | The returned point approximates an intersection; residuals show equation accuracy. |
| 13 — Interpolation | Seven hourly sensor measurements; estimate values with linear and cubic interpolation. | The value at 2.5 hours is inferred between measurements; the graph compares smoothness and fit. |
| 14 — Curve fitting | Concurrent user counts and response-time observations; fit a straight line with least squares. | The intercept and slope summarize the trend; R² indicates the fraction of variation explained by the line. |
| 15 — Numerical differentiation | GPS positions at one-second intervals; use forward, central, and backward finite differences. | Printed values estimate instantaneous speed; the graph shows how speed changes over time. |
| 16 — Numerical integration | Seven smart-meter power readings every two hours; integrate with trapezoidal and Simpson rules. | Each result estimates energy used in kWh; their difference shows sensitivity to the approximation method. |
| 17 — Euler ODE | Initial object temperature 90 °C, ambient 25 °C, cooling constant 0.12/min, one-minute step; apply Euler’s method. | The final estimate predicts temperature after 30 minutes; comparison with the exact curve shows step-size error. |
| 18 — SciPy ODE | RC circuit with 5 V supply, 1000 Ω resistance and 0.001 F capacitance; solve with `solve_ivp`. | Voltage rises toward the supply voltage; solver status and exact-solution error assess the result. |
| 19 — Optimization | Two server types with differing costs and capacities; minimize cost subject to capacity ≥1000 and nonnegative allocations. | The continuous result is a planning allocation; enumeration also reports the least-cost whole-server combination. |
| 20 — Monte Carlo | 100,000 seeded demand values from a normal model (mean 850, standard deviation 120) against capacity 1000. | The overload fraction estimates overload probability; the graph shows its running estimate as samples accumulate. |

## Required parameter change

Several scripts allow the inputs to be changed at the top of the file. For example, changing `step` in Task 17 changes Euler’s time resolution: smaller steps generally reduce discretization error and require more updates. Changing `simulations` in Task 20 changes Monte Carlo precision: more scenarios generally stabilize the estimated overload probability, at a greater computation cost. The outputs and plots are intended to make these effects observable.

## Related real-world case (Task 21)

### Cold-chain medicine transport

`code/Task_21_cold_chain.py` adapts the ODE method from Task 18 to compare two medicine containers during a 12-hour trip in a 32 °C environment.

- **Assumptions:** The medicine starts at 8 °C; ambient temperature stays constant; container warming follows Newton’s law, `dT/dt = k(T_ambient − T)`; the standard container has `k=0.18/hour`, and insulation reduces it to `k=0.07/hour`. The illustrative maximum target is 10 °C.
- **Inputs:** ambient and initial temperatures, target temperature, trip duration, and the two warming-rate constants are defined in the script.
- **Operation:** SciPy `solve_ivp` calculates the temperature trajectory for each container. The script reports final temperature and the approximate time the threshold is crossed, then plots both trajectories.
- **Interpretation:** A lower warming rate means the medicine stays cooler for longer. Compare the threshold crossing times to see which container better preserves the assumed temperature limit during transport.
- **Parameter change:** Change `cooling_rates` (warming-rate constants) to represent different insulation or handling conditions. A lower constant delays threshold crossing; a higher constant brings medicine closer to ambient temperature faster.

This is a simplified demonstration model. It assumes constant ambient conditions and one uniform warming rate for the entire trip.
