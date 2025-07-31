color_map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors):
    first_color = color_map[colors[0]]
    second_color = color_map[colors[1]]
    value = f"{str(first_color)}{str(second_color)}"
    return int(value)
