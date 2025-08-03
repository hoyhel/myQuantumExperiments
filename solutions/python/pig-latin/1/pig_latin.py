def translate(text):
    VOWELS = "aeiou"
    SPECIAL = ("xr", "yt")

    def starts_with_vowel_or_special(word):
        return word.startswith(SPECIAL) or word[0] in VOWELS

    def find_consonant_qu(word):
        # Look for "qu" after leading consonants
        for j in range(len(word) - 1):
            if word[j:j+2] == "qu" and all(c not in VOWELS for c in word[:j]):
                return j + 2
        return None

    def find_consonants_then_y(word):
        for i in range(1, len(word)):
            if word[i] == "y" and all(c not in VOWELS for c in word[:i]):
                return i
        return None

    def leading_consonant_cluster(word):
        i = 0
        while i < len(word) and word[i] not in VOWELS:
            if word[i] == 'y' and i != 0:
                break
            i += 1
        return i

    def translate_word(word):
        if starts_with_vowel_or_special(word):
            return word + "ay"
        idx_qu = find_consonant_qu(word)
        if idx_qu:
            return word[idx_qu:] + word[:idx_qu] + "ay"
        idx_y = find_consonants_then_y(word)
        if idx_y:
            return word[idx_y:] + word[:idx_y] + "ay"
        cluster_len = leading_consonant_cluster(word)
        return word[cluster_len:] + word[:cluster_len] + "ay"

    return ' '.join(translate_word(w) for w in text.split())