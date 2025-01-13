# Adapted from InfoWorld's video:
# https://youtu.be/xw-8XBuTrIg?si=NwayEo4DEn-V4ARJ


def transform(n: int) -> int:
    q = 0
    for x in range(0, n * 500):
        q += x
    return q


if __name__ == "__main__":
    import time

    limit = 1_000

    start = time.perf_counter_ns()
    result = sum([transform(x) for x in range(limit)])
    end = time.perf_counter_ns()

    print(f"Result: {result} (in {(end - start) * 1e-9:,.3f} s)")
