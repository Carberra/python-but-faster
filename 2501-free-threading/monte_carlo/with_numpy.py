import numpy as np


def monte_carlo_pi(samples: int) -> float:
    points = np.random.random((samples, 2))
    acc = np.sum(((points[:, 0] ** 2) + (points[:, 1] ** 2)) < 1.0)
    return 4.0 * acc / samples


if __name__ == "__main__":
    import time

    points = 10_000_000

    start = time.perf_counter_ns()
    pi = monte_carlo_pi(points)
    end = time.perf_counter_ns()

    print(f"Pi: {pi} (in {(end - start) * 1e-9:,.3f} s)")
