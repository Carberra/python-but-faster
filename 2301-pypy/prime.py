def is_prime(n: int) -> bool:
    for i in range(2, n):  # sourcery skip: invert-any-all, use-any, use-next
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n: int):
    return [i for i in range(n) if is_prime(i)]
