def score(word):
    points_dict = {1: ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"], 2: ["d", "g"], 3: ["b", "c", "m", "p"], 4: ["f", "h", "v", "w", "y"], 5: ["k"], 8: ["j", "x"], 10: ["q", "z"]}
    
    word_lower = word.lower()
    points = 0

    for wl in word_lower:
        for key in points_dict:
            for value in points_dict[key]:
                if wl == value:
                    points += key

    return points
