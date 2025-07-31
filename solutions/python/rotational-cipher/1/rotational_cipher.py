import string

def rotate(text, key):
    # Create the new variables
    small_letters = list(string.ascii_lowercase)
    capital_letters = list(string.ascii_uppercase)
    new_text = ""
    
    # Loop through each character in the text variable
    for char in text:
        # Check if the character is an alphabet
        if char in small_letters:
            index = small_letters.index(char)
            new_index = (index + key) % 26
            new_text += small_letters[new_index]
        elif char in capital_letters:
            index = capital_letters.index(char)
            new_index = (index + key) % 26
            new_text += capital_letters[new_index]
        # If not, do what
        else:
            new_text += char

    # Return the new string variable
    return new_text