def is_pangram(sentence):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(sentence.lower())
