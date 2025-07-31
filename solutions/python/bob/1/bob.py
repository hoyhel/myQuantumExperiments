def response(hey_bob):
    stripped = hey_bob.strip()

    if stripped:
        if stripped[-1] == "?" and not stripped.isupper():
            return "Sure."
        elif stripped.isupper() and stripped[-1] != "?":
            return "Whoa, chill out!"
        elif stripped[-1] == "?" and stripped.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Whatever."
    else:
        return "Fine. Be that way!"
    
