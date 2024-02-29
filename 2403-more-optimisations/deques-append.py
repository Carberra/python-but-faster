from collections import deque
from timeit import repeat

numbers: list[int] = []
numbers_populated = [*range(1000)]

t0 = min(
    repeat(
        """
for i in range(10):
    numbers.append(i)
""",
        globals={"numbers": numbers.copy()},
    )
)
t1 = min(
    repeat(
        """
for i in range(10):
    numbers.append(i)
""",
        globals={"numbers": deque(numbers)},
    )
)

print(
    f"""
APPENDING TO RIGHT
Lists:  {t0:.3f}
Deques: {t1:.3f}
"""
)


t0 = min(
    repeat(
        """
for i in range(10):
    numbers.insert(0, i)
""",
        globals={"numbers": numbers.copy()},
        number=5000,
    )
)
t1 = min(
    repeat(
        """
for i in range(10):
    numbers.appendleft(i)
""",
        globals={"numbers": deque(numbers)},
        number=5000,
    )
)

print(
    f"""
APPENDING TO LEFT
Lists:  {t0:.3f}
Deques: {t1:.3f}
"""
)
