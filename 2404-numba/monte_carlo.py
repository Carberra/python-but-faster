import random

from numba import jit, njit


@njit
def monte_carlo_pi(nsamples):
    acc = 0
    for _ in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


if __name__ == "__main__":
    import time

    t0 = time.perf_counter_ns()
    pi = monte_carlo_pi(100_000_000)
    t1 = time.perf_counter_ns()
    print(f"Pi = '{pi}' in {(t1 - t0) / 1_000_000:,.0f}ms")
