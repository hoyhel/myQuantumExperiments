def rebase(input_base, digits, output_base):
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Converting from input base to base 10
    base_ten_total = 0
    for index, digit in enumerate(reversed(digits)):
        summed = digit * input_base ** index
        base_ten_total += summed

    # Converting from base 10 to output base
    remainders = []
    if not digits or all(item == 0 for item in digits):
        remainders = [0]
    while base_ten_total != 0:
        remainder = base_ten_total % output_base
        remainders.append(remainder)
        base_ten_total //= output_base
    remainders.reverse()
    return remainders