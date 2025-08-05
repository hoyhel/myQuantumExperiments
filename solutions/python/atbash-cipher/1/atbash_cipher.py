# Lists of alphabets and numbers
normal = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipher = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def encode(plain_text):
    # Create a variable to store the new string
    new_text = ""
    
    # Loop through each character in the string 
    for char in plain_text.lower():
        if char in normal:
            index = normal.index(char) # Find index
            new_text += cipher[index] # Add the equivalent item from the other list
        elif char in numbers:
            new_text += char

    groups = [new_text[i:i+5] for i in range(0, len(new_text), 5)]
    return " ".join(groups)


def decode(ciphered_text):
    # Create a variable to store the new string
    new_ciphered_text = ""

    # Loop through each character in the string
    for char in ciphered_text:
        if char in cipher:
            index = cipher.index(char)
            new_ciphered_text += normal[index]
        elif char in numbers:
            new_ciphered_text += char
            
    return new_ciphered_text
