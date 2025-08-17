def transpose(text):
    if not text:
        return ""

    lines = text.split("\n")
    max_len = max((len(line) for line in lines), default=0)

    # Pad lines to the right
    padded = [line.ljust(max_len) for line in lines]

    result_rows = []
    for col_idx in range(max_len):
        # build this transposed row
        col_chars = [row[col_idx] for row in padded]

        # find how far we should keep (last non-space is determined by real line length)
        last_non_space = 0
        for row_idx, line in enumerate(lines):
            if col_idx < len(line):   # this row actually had a character here
                last_non_space = row_idx

        # slice only up to that last contributing row
        row_str = "".join(col_chars[:last_non_space + 1])
        result_rows.append(row_str)

    return "\n".join(result_rows)
