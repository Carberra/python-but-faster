from functools import cache
from timeit import timeit


@cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


t0 = timeit("f(40)", globals={"f": fibonacci}, number=1)
print(f"{t0:.6f}")
