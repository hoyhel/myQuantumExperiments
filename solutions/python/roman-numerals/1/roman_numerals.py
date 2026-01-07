def roman(number):
    letters = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    lookup_values = [
        1000, 900, 500, 400,
         100,  90,  50,  40,
          10,   9,   5,   4,
           1
    ]
    result = ""
    index = 0
    while number:
        while number >= lookup_values[index]:
            number -= lookup_values[index]
            result += letters[index]
        index += 1
    return result
