def answer(question):

    # Remove the question mark
    question = question.replace("?", "")

    # Split the question
    words = question.split()

    words_to_remove = ["What", "is", "by"]

    # Remove 'What' and 'is'
    remaining_words = []
    for word in words:
        if word not in words_to_remove:
            remaining_words.append(word)

    # Turn numbers into integers
    for index, item in enumerate(remaining_words):
        if item.lstrip("-").isdigit():
            remaining_words[index] = int(item)

    acceptable_operations = ['plus', 'minus', 'multiplied', 'divided']

    result = 0
    # Check the operation in the 1st index of the list
    if len(remaining_words) == 1:
        return remaining_words[0]
    elif (len(remaining_words) == 3 or len(remaining_words) == 5) and isinstance(remaining_words[1], str):
        if remaining_words[1] == "plus":
            result = remaining_words[0] + remaining_words[2]
        elif remaining_words[1] == "minus":
            result = remaining_words[0] - remaining_words[2]
        elif remaining_words[1] == "multiplied":
            result = remaining_words[0] * remaining_words[2]
        elif remaining_words[1] == "divided":
            result = remaining_words[0] // remaining_words[2]
    elif len(remaining_words) == 2 and remaining_words[1] not in acceptable_operations:
        raise ValueError("unknown operation")
    else:
        raise ValueError("syntax error")
    if len(remaining_words) == 5:
        if remaining_words[3] == "plus":
            result += remaining_words[4]
        elif remaining_words[3] == "minus":
            result -= remaining_words[4]
        elif remaining_words[3] == "multiplied":
            result *= remaining_words[4]
        elif remaining_words[3] == "divided":
            result //= remaining_words[4]
    return result