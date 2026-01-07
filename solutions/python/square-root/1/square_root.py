def square_root(number):
    if number > 4:
        half = number // 2
    else:
        half = number

    var_square_root = ""
    for num in range(half + 1):
        if num * num == number:
            var_square_root = num
    return var_square_root
