def is_paired(input_string):
    # Initialise an empty stack.
    stack = []
    # Create a mapping of closing brackets to their corresponding opening brackets.
    matches = {']': '[', '}': '{', ')':'('}
    # Loop through each character in the input string.
    for str in input_string:
    # If the character is an opening bracket, push it onto the stack.
        if str in matches.values():
            stack.append(str)
    # If the character is a closing bracket:
        elif str in matches:
        # Check if the stack is empty.
            if not stack:
                # Return False if so.
                return False
        # Otherwise pop the top element from the stack.
            else:
                last = stack.pop()
        # Check if it matches the expected opening bracket.
                if matches[str] != last:
                    return False
        # Return False if not.

    # After looping check if the stack is empty.
    # If so, all brackets have been matched. Return True.
    if not stack:
        return True
    # False otherwise.
    else:
        return False
