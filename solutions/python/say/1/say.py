def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    num_to_19 = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    scales = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
        (1, "")
    ]

    def convert_hundreds(n):
        parts = []
        if n >= 100:
            parts.append(num_to_19[n // 100] + " hundred")
            n %= 100
        if n >= 20:
            parts.append(tens[n // 10] + ("-" + num_to_19[n % 10] if n % 10 else ""))
        elif n > 0:
            parts.append(num_to_19[n])
        return " ".join(parts)

    result = []
    for scale_value, scale_name in scales:
        chunk = number // scale_value
        if chunk:
            number -= chunk * scale_value
            chunk_words = convert_hundreds(chunk)
            if scale_name:
                chunk_words += f" {scale_name}"
            result.append(chunk_words)

    return " ".join(result)
