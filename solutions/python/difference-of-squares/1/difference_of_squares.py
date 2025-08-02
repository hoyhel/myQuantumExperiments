def square_of_sum(number):
    numbers_list = []

    for num in range(number + 1):
        numbers_list.append(num)

    return sum(numbers_list) ** 2


def sum_of_squares(number):
    numbers_list = []

    for num in range(number + 1):
        numbers_list.append(num ** 2)

    return sum(numbers_list)
        

def difference_of_squares(number):
    square_sum = square_of_sum(number)
    sum_square = sum_of_squares(number)

    return square_sum - sum_square
