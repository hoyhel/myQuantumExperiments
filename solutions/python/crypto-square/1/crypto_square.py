def cipher_text(plain_text):
    normalised_text = ""
    for character in plain_text:
        if character.isalpha() or character.isdigit():
            normalised_text += character.lower()

    # Get the rectangle dimensions
    length_of_text = len(normalised_text)
    r = int(length_of_text ** 0.5)
    c = r
    if r * c < length_of_text:
        c += 1
    if r * c < length_of_text:
        r += 1

    # Create the rectangular string using the dimensions found.
    rectangle_string = []
    normalised_text_chars = list(normalised_text)
    for row in range(r):
        current_row = ""
        for column in range(c):
            if normalised_text_chars:
                char = normalised_text_chars.pop(0)
                current_row += char
            else:
                current_row += " "
        rectangle_string.append(current_row)

    # Transpose that list to make another one.
    transposed_rectangle_string = []
    row_num = 0
    col_num = 0
    while row_num < c: # 8 iterations
        current_row = ""
        row = 0
        while row < r:
            line = rectangle_string[row]
            char = line[col_num]
            current_row += char
            row += 1
        transposed_rectangle_string.append(current_row)
        row_num += 1
        col_num += 1

    # Return the final string format of the encoded text.
    final_text = ""
    for index, row in enumerate(transposed_rectangle_string):
        if index == len(transposed_rectangle_string) - 1:
            final_text += row
        else:
            final_text += row + " "
    return final_text