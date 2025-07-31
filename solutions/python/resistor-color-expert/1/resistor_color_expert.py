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

tolerance_map = {
    "brown": "±1%",
    "red": "±2%",
    "green": "±0.5%",
    "blue": "±0.25%",
    "violet": "±0.1%",
    "grey": "±0.05%",
    "gold": "±5%",
    "silver": "±10%"
}

def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    if len(colors) == 5:
        # 5-band: 3 digits, 1 multiplier, 1 tolerance
        digits = f"{color_map[colors[0]]}{color_map[colors[1]]}{color_map[colors[2]]}"
        multiplier = 10 ** color_map[colors[3]]
        tolerance = tolerance_map.get(colors[4], "")
    elif len(colors) == 4:
        # 4-band: 2 digits, 1 multiplier, 1 tolerance
        digits = f"{color_map[colors[0]]}{color_map[colors[1]]}"
        multiplier = 10 ** color_map[colors[2]]
        tolerance = tolerance_map.get(colors[3], "")
    else:
        raise ValueError("Invalid number of color bands")

    resistance = int(digits) * multiplier

    # Format resistance with metrix prefix
    if resistance >= 1_000_000_000:
        value = resistance / 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    # Format: strip .00 if it's a whole number
    if isinstance(value, float) and value.is_integer():
        value = int(value)

    display = f"{value} {unit}"
    return f"{display} {tolerance}".strip()
        