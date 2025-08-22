def primes(limit):
    if limit < 2:
        return []
    primes_list = [False] * 2 + [True] * (limit - 1)

    for p in range(2, int(limit ** 0.5) + 1):
        if primes_list[p]:
            for i in range(p * p, limit + 1, p):
                primes_list[i] = False

    result = [i for i in range(2, limit + 1) if primes_list[i]]
    return result
