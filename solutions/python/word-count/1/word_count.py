import re
from collections import Counter

def count_words(sentence):
    pattern = r"(?:\s+|[^A-Za-z0-9']|(?<![A-Za-z0-9])'|'(?![A-Za-z0-9]))"
    raw_words = re.split(pattern, sentence)
    words = [re.sub(r"^'+|'+$", "", w) for w in raw_words if w]
    for index, word in enumerate(words):
        words[index] = word.lower()

    counts = Counter(words)
    return counts
