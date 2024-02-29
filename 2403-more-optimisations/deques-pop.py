from collections import deque
from timeit import timeit

numbers = [*range(100_000)]

t0 = timeit(
    """
for i in range(len(numbers)):
    numbers.pop()
""",
    globals={"numbers": numbers.copy()},
)
t1 = timeit(
    """
for i in range(len(numbers)):
    numbers.pop()
""",
    globals={"numbers": deque(numbers)},
)


print(
    f"""
POPPING FROM RIGHT
Lists:  {t0:.3f}
Deques: {t1:.3f}
"""
)


t0 = timeit(
    """
for i in range(len(numbers)):
    numbers.pop(0)
""",
    globals={"numbers": numbers.copy()},
)
t1 = timeit(
    """
for i in range(len(numbers)):
    numbers.popleft()
""",
    globals={"numbers": deque(numbers)},
)


print(
    f"""
POPPING FROM LEFT
Lists:  {t0:.3f}
Deques: {t1:.3f}
"""
)
