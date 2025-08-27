def convert(input_grid):
    # Validate grid size
    if not input_grid or len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if input_grid and any(len(row) % 3 != 0 or len(row) != len(input_grid[0]) for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    # Digit patterns (3x4 grid as single string, exact spacing)
    patterns = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",  # Fixed pattern for 8
        " _ |_| _|   ": "9"
    }

    # Process each 4-row group
    result = []
    for i in range(0, len(input_grid), 4):
        rows = input_grid[i:i+4]
        num_digits = len(rows[0]) // 3 if rows else 0
        line_result = ""
        
        # Process each 3-column chunk
        for j in range(num_digits):
            # Extract 3x4 block (rows 0–3, columns j*3 to (j+1)*3)
            block = "".join(row[j*3:(j+1)*3] for row in rows)
            line_result += patterns.get(block, "?")
        
        result.append(line_result)
    
    # Join lines with commas
    return ",".join(result) if result else ""