def spiral_matrix(size):
    # 1. Create an n x n matrix filled with zeros.
    if size == 0:
        return []
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # 2. & 3. Initialize counter and boundary pointers.
    counter = 1
    top, bottom = 0, size - 1
    left, right = 0, size - 1

    # 4. Start the main loop.
    while top <= bottom and left <= right:
        # 5a. Fill the top row (Go Right)
        for i in range(left, right + 1):
            matrix[top][i] = counter
            counter += 1
        top += 1 # Move top boundary down

        # 5b. Fill the right column (Go Down)
        for i in range(top, bottom + 1):
            matrix[i][right] = counter
            counter += 1
        right -= 1 # Move right boundary in

        # 5c. Fill the bottom row (Go Left)
        # We need to check if the boundaries have crossed
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = counter
                counter += 1
            bottom -= 1 # Move bottom boundary up

        # 5d. Fill the left column (Go Up)
        # We need to check if the boundaries have crossed
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = counter
                counter += 1
            left += 1 # Move left boundary in

    # 7. Return the result.
    return matrix