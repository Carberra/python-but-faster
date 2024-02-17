import json
import pathlib
from timeit import timeit

x = json.loads(pathlib.Path("data.json").read_text())
setup_sort = pathlib.Path("sort.py").read_text()
t_sort = timeit("sort(x)", setup=setup_sort, globals={"x": x}, number=1_000)
print(f"  Sorting: {t_sort:.3f}s")

setup_prime = pathlib.Path("prime.py").read_text()
t_prime = timeit(
    "get_primes_up_to(x)", setup=setup_prime, globals={"x": 10_000}, number=100
)
print(f"   Primes: {t_prime:.3f}s")

setup_fact = pathlib.Path("fact.py").read_text()
t_fact = timeit("factorial(x)", setup=setup_fact, globals={"x": 10_000}, number=500)
print(f"Factorial: {t_fact:.3f}s")
