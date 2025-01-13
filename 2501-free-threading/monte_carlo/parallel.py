import random
import time
from concurrent.futures import ThreadPoolExecutor


def monte_carlo_pi(samples: int) -> float:
    inside = 0
    for _ in range(samples):
        x = 0.5
        y = 0.5
        if (x**2 + y**2) < 1.0:
            inside += 1
    return 4.0 * inside / samples


def parallel_monte_carlo(total_points: int, num_threads: int) -> float:
    points_per_thread = total_points // num_threads

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(monte_carlo_pi, points_per_thread)
            for _ in range(num_threads)
        ]
        results = [future.result() for future in futures]

    pi_estimate = sum(results) / len(results)
    return pi_estimate


if __name__ == "__main__":
    import time

    points = 10_000_000
    threads = 10

    start = time.perf_counter_ns()
    pi = parallel_monte_carlo(points, threads)
    end = time.perf_counter_ns()

    print(f"Pi: {pi} (in {(end - start) * 1e-9:,.3f} s)")
