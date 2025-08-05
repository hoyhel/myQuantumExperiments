def factors(value):
    divider = 2
    result = []

    while value != 1:
        if value % divider == 0:
            result.append(divider)
            value = value // divider
        else:
            divider += 1

    return result
