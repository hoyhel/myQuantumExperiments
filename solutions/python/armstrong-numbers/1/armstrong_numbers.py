def is_armstrong_number(number):
    power = len(str(number))
    total = sum(int(digit) ** power for digit in str(number))
    return total == number
