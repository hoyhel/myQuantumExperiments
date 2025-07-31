def find_anagrams(word, candidates):
    # Convert 'word' to lower case
    word = word.lower()
    sorted_word = "".join(sorted(word))
    anagrams = []
    # Loop through each candidate
    for candidate in candidates:
    # Convert each candidate to lowercase
        candidate_original = candidate
        candidate = candidate.lower()
    # Check if the candidate is the same as the word, skip it then
        if candidate == word:
            continue
    # Otherwise proceed with sorting the candidate letters
    # Compare the sorted candidate with the sorted target
        else:
            sorted_candidate = "".join(sorted(candidate))
    # If they match, it's an anagram
            if sorted_candidate == sorted_word:
                anagrams.append(candidate_original)

    return anagrams
    