def is_valid(isbn):
    # Remove dashes
    isbn = isbn.replace("-", "")

    # Check length
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(10):
        char = isbn[i]

        if i == 9 and char.upper() == "X":
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
             return False

        total += (i + 1) * value

    return total % 11 == 0
