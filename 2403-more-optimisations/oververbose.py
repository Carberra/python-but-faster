from timeit import timeit

verbose = """
while len(numbers) > 0:
    numbers.pop()
"""

simple = """
while numbers:
    numbers.pop()
"""

for i in range(9):
    numbers = [*range(10**i)]

    t0 = timeit(verbose, globals={"numbers": numbers.copy()})
    t1 = timeit(simple, globals={"numbers": numbers.copy()})

    print(
        f"""For 1e{i}:
    Verbose: {t0:.3f}
    Simple: {t1:.3f}
    """
    )

input("Press ENTER to continue")

import dis

print("-" * 80)
dis.dis(verbose)
print("-" * 80)
dis.dis(simple)
