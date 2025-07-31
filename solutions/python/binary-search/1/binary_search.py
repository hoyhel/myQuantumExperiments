def find(search_list, value):
    start = 0
    end = len(search_list) - 1

    while start <= end:
        middle = (start + end) // 2
        middle_value = search_list[middle]

        if middle_value == value:
            return middle
        elif middle_value < value:
            start = middle + 1
        else:
            end = middle - 1

    raise ValueError("value not in array")
