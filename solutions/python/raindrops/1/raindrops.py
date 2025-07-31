def convert(number):
    if number % 3 == 0:
        if number % 3 == 0 and number % 5 == 0:
            if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
                return "PlingPlangPlong"
            return "PlingPlang"
        if number % 3 == 0 and number % 7 == 0:
            return "PlingPlong"
        return "Pling"
    if number % 5 == 0:
        if number % 5 == 0 and number % 7 == 0:
            return "PlangPlong"
        return "Plang"
    if number % 7 == 0:
        return "Plong"
    else: 
        return f"{number}"
