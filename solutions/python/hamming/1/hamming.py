def distance(strand_a, strand_b):
    # Make lists for both strands storing each letter.
    # Create a difference integer variable to store the differences.
    strand_a_list = list(strand_a)
    strand_b_list = list(strand_b)
    difference = 0

    # Check if the length of both strands are not equal.
    if len(strand_a_list) != len(strand_b_list):
        raise ValueError("Strands must be of equal length.")
        
    for i in range(len(strand_a_list)):
        if strand_a_list[i] != strand_b_list[i]:
            difference +=1

    # Return difference
    return difference
