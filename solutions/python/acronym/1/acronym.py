import re

def abbreviate(words):
    allowed = "-"
    cleaned = "".join(char for char in words if char.isalnum() or char.isspace() or char in allowed)
    group = re.split(r"[\s\-]+", cleaned)

    string = ""
    for word in group:
        string += word[0].upper()

    return string