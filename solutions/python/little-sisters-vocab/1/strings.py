"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    return f' :: {prefix}'.join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # Remove 'ness' and if the word ends in a consonant and then 'i', change it to 'y'.

    # Store the word without 'ness'.
    without_ness = word[:-4]

    # Check if the second last character is a consonant AND the last character is a vowel.
    # If so, change the variable to 'y'.
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    second_last_char = without_ness[-2]
    last_char = without_ness[-1]

    if second_last_char in consonants and last_char in vowels:
        modified_word = without_ness.replace(last_char, 'y')
        return modified_word

    return without_ness


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    # Split the sentence and remove the trailing full stop.
    split_sentence = sentence.split()
    split_sentence[-1] = split_sentence[-1].rstrip('.')

    # Locate the adjective using the index argument.
    adjective = split_sentence[index]

    # add 'en' to the end of the word.
    verb = adjective + 'en'

    return verb
