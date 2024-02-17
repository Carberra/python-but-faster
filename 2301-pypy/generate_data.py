import json
import random

x = [random.randint(1, 100) for _ in range(1000)]

with open("data.json", "w") as f:
    json.dump(x, f)
