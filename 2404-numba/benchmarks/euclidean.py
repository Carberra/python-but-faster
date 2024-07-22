from timeit import repeat

from numba import jit, njit
from tabulate import tabulate

POINTS = [(0, 0), (3, 4)]


def euclidean_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


@jit
def euclidean_distance_jit(a: tuple[float, float], b: tuple[float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


@njit
def euclidean_distance_njit(a: tuple[float, float], b: tuple[float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


if __name__ == "__main__":
    t0 = (
        min(
            repeat(
                "euclidean_distance(*points)",
                setup="from __main__ import euclidean_distance",
                globals={"points": POINTS},
            )
        )
        * 1000
    )
    t1 = (
        min(
            repeat(
                "euclidean_distance_jit(*points)",
                setup="from __main__ import euclidean_distance_jit; from numba import jit",
                globals={"points": POINTS},
            )
        )
        * 1000
    )
    t2 = (
        min(
            repeat(
                "euclidean_distance_njit(*points)",
                setup="from __main__ import euclidean_distance_njit; from numba import njit",
                globals={"points": POINTS},
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
