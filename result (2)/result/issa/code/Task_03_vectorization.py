import timeit
import numpy as np

rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)
def loop_version():
    return [(value / 1000.0) ** 2 for value in latency_ms]
def vectorized_version():
    return (latency_ms / 1000.0) ** 2
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()
print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")
