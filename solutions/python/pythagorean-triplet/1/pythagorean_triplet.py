def triplets_with_sum(number):
    if number < 12:
        return []

    result = []
    for a in range(1, number//3 + 1):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if b < c and a * a + b * b == c * c:
                result.append([a, b, c])
    return result