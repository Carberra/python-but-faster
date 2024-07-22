import random
from timeit import repeat

from tabulate import tabulate

SAMPLES = 100_000_000


def monte_carlo_pi(nsamples):
    acc = 0
    for _ in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


if __name__ == "__main__":
    t0 = (
        min(
            repeat(
                "monte_carlo_pi(samples)",
                setup="from __main__ import monte_carlo_pi",
                globals={"samples": SAMPLES},
                number=1,
            )
        )
        * 1000
    )
    t1 = (
        min(
            repeat(
                "jit(monte_carlo_pi)(samples)",
                setup="from __main__ import monte_carlo_pi; from numba import jit",
                globals={"samples": SAMPLES},
                number=1,
            )
        )
        * 1000
    )
    t2 = (
        min(
            repeat(
                "njit(monte_carlo_pi)(samples)",
                setup="from __main__ import monte_carlo_pi; from numba import njit",
                globals={"samples": SAMPLES},
                number=1,
            )
        )
        * 1000
    )

    fastest = min(t0, t1, t2)

    table = [
        ["None", t0, t0 / fastest],
        ["jit", t1, t1 / fastest],
        ["njit", t2, t2 / fastest],
    ]
    print(
        tabulate(
            table,
            headers=["Decorator", "Time (ms)", "Vs. fastest"],
            floatfmt=",.2f",
        )
    )
