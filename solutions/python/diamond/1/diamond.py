def rows(letter):
    num_of_spaces = {"A": 0,
                    "B": 1,
                    "C": 3,
                    "D": 5,
                    "E": 7,
                    "F": 9,
                    "G": 11,
                    "H": 13,
                    "I": 15,
                    "J": 17,
                    "K": 19,
                    "L": 21,
                    "M": 23,
                    "N": 25,
                    "O": 27,
                    "P": 29,
                    "Q": 31,
                    "R": 33,
                    "S": 35,
                    "T": 37,
                    "U": 39,
                    "V": 41,
                    "W": 43,
                    "X": 45,
                    "Y": 47,
                    "Z": 49}

    # Create the list to store the letter and space combinations
    diamond = []

    middle = ""
    middle += letter
    if middle != "A":
        for space in range(num_of_spaces[letter]):
            middle += " "
        middle += letter
    diamond.append(middle)

    # First, find the index of the current letter given.
    # Find the previous letter
    keys_list = list(num_of_spaces.keys())
    index = keys_list.index(letter)

    while index > 0:
        if index == 0:
            continue
        else:
            index = index - 1
            if index == 0:
                next_item = keys_list[index]
            else:
                next_item = keys_list[index]
                for space in range(num_of_spaces[next_item]):
                    next_item += " "
                next_item += keys_list[index]

        # Find the number of spaces to add outside each letter
        # Add those
        length = len(next_item)
        difference = len(middle) - length
        # Find the number of spaces to add on each side
        num_space_each_side = difference // 2
        char_list = list(next_item)

        # Add those spaces
        for i in range(num_space_each_side):
            char_list = [" "] + char_list
        for i in range(num_space_each_side):
            char_list = char_list + [" "]

        new_next_item = "".join(char_list)
        diamond.append(new_next_item)

    other_half = diamond[:]
    del other_half[0]
    other_half.reverse()
    diamond = other_half + diamond

    return diamond

var = rows("A")
print(var)
