import random
from timeit import repeat

import numpy as np

lst = [random.randint(1, 100) for _ in range(1_000)]
arr = np.array(lst)

t0 = min(repeat("[x for x in lst if x % 2 == 0]", globals={"lst": lst}, number=100_000))
t1 = min(repeat("arr[arr % 2 == 0]", globals={"arr": arr}, number=100_000))

print(
    f"""
List:  {t0:.3f}
Array: {t1:.3f}
"""
)
