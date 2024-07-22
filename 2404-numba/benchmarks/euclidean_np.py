from timeit import repeat

import numpy as np
from numba import jit, njit
from tabulate import tabulate

POINTS = np.array([(0, 0), (3, 4)])


def euclidean_distance(points: np.ndarray) -> float:
    return np.sqrt(np.sum((points[0] - points[1]) ** 2))


@jit
def euclidean_distance_jit(points: np.ndarray) -> float:
    return np.sqrt(np.sum((points[0] - points[1]) ** 2))


@njit
def euclidean_distance_njit(points: np.ndarray) -> float:
    return np.sqrt(np.sum((points[0] - points[1]) ** 2))


if __name__ == "__main__":
    t0 = (
        min(
            repeat(
                "euclidean_distance(points)",
                setup="from __main__ import euclidean_distance; import numpy as np",
                globals={"points": POINTS},
            )
        )
        * 1000
    )
    t1 = (
        min(
            repeat(
                "euclidean_distance_jit(points)",
                setup="from __main__ import euclidean_distance_jit; from numba import jit; import numpy as np",
                globals={"points": POINTS},
            )
        )
        * 1000
    )
    t2 = (
        min(
            repeat(
                "euclidean_distance_njit(points)",
                setup="from __main__ import euclidean_distance_njit; from numba import njit; import numpy as np",
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
