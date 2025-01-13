import random


def monte_carlo_pi(samples: int) -> float:
    inside = 0
    for _ in range(samples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            inside += 1
    return 4.0 * inside / samples


if __name__ == "__main__":
    import time

    points = 10_000_000

    start = time.perf_counter_ns()
    pi = monte_carlo_pi(points)
    end = time.perf_counter_ns()

    print(f"Pi: {pi} (in {(end - start) * 1e-9:,.3f} s)")
