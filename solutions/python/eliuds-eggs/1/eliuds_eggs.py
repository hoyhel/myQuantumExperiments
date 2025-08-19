def egg_count(display_value):
    remainders = ""
    while display_value != 0:
        remainders += str(display_value % 2)
        display_value = display_value // 2
    binary = remainders[::-1]

    one_counts = binary.count("1")
    return one_counts
