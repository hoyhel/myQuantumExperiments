def decode(string): # "12WB12W3B24WB"
    result = ""
    i = 0

    while i < len(string):
        if string[i].isdigit():
            # Start reading the full number (in case it's multiple digits)
            num_str = ""
            while i < len(string) and string[i].isdigit():
                num_str += string[i]
                i += 1
            count = int(num_str)

            # After the full number, the next character must be a letter
            if i < len(string):
                result += string[i] * count
        else:
            # Only add the letter if the previous character is not a digit
            if i == 0 or not string[i - 1].isdigit():
                result += string[i]
        i += 1

    return result
    


def encode(string):
    current_letter = "" 
    num_of_letters = "" 
    final_string = ""

    for index, char in enumerate(string): 
        if not current_letter: # If current_letter is empty. Runs only in the beginning
            current_letter = char # Assign that new letter to current_letter
            num_of_letters = 1 # Start keeping track of the frequency
        else: # Runs when current_letter isn't empty
            if char == current_letter: # If the current letter being looped is equals to the stored letter in current_letter
                num_of_letters += 1 # If so, add one to num_of_letters to
            else: # If it's not equal. The place to add the result to final_string and reset the values of both variables
                if num_of_letters == 1: # If one, only the letter should be added
                    final_string += current_letter
                else: # Otherwise, mention the number too
                    final_string += f"{num_of_letters}{current_letter}"
                    # Reset the values
                current_letter = char
                num_of_letters = 1
            if index == len(string) - 1:
                if num_of_letters == 1: # If one, only the letter should be added
                    final_string += current_letter
                else: # Otherwise, mention the number too
                    final_string += f"{num_of_letters}{current_letter}"
                    # Reset the values
                current_letter = ""
                num_of_letters = ""
    return final_string
