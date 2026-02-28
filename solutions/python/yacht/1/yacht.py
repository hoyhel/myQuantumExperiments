YACHT = "YACHT"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
    points = 0
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        points = dice.count(category) * category
    elif category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]:
        points = 30
    elif category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]:
        points = 30
    elif category == CHOICE:
        points = sum(dice)
    else:
        faces = {}
        for die in dice:
            faces[die] = faces.get(die, 0) + 1
        if category == FULL_HOUSE and sorted(faces.values()) == [2, 3]:
            points = sum(dice)
        elif category == FOUR_OF_A_KIND:
            for die, count in faces.items():
                if count >= 4:
                    points = 4 * die
        elif category == YACHT and 5 in faces.values():
            points = 50
    return points
