from numba import jit, njit

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
    from time import perf_counter_ns

    t0 = perf_counter_ns()
    euclidean_distance(*POINTS)
    t1 = perf_counter_ns()
    euclidean_distance_njit(*POINTS)
    t2 = perf_counter_ns()
    euclidean_distance_jit(*POINTS)
    t3 = perf_counter_ns()

    print(f"{t1 - t0:,.0f}")
    print(f"{t2 - t1:,.0f}")
    print(f"{t3 - t2:,.0f}")
