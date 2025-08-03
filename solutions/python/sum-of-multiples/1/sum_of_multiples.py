def sum_of_multiples(limit, multiples):
    if limit <= 0:
        return 0

    energy_points = set()

    for base in multiples:
        if base == 0:
            continue  # Skip zero to avoid infinite loops or division errors
        for i in range(base, limit, base):
            energy_points.add(i)

    return sum(energy_points)
