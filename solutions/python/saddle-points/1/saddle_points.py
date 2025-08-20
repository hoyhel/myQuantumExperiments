def saddle_points(matrix):
    # Step 1: Check if matrix is empty
    if not matrix:
        return []
    
    # Step 2: Check for irregular matrix
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("irregular matrix")
    
    results = []
    num_rows = len(matrix)
    
    # Step 3 and 4: Find saddle points
    for i, row in enumerate(matrix):
        max_in_row = max(row)
        for j, value in enumerate(row):
            if value == max_in_row:
                # Check if value is the minimum in its column
                col_values = [matrix[x][j] for x in range(num_rows)]
                if value == min(col_values):
                    # 1-based indexing for row and column
                    results.append({'row': i + 1, 'column': j + 1})
                    
    return results

