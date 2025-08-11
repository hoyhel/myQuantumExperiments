def proverb(*words_list, qualifier=None):
    proverbs = []
    word_2 = 1

    for index, word in enumerate(words_list):
        if len(words_list) == 1 or len(words_list) == 0:
            break

        sentence = f"For want of a {word} the {words_list[word_2]} was lost."

        negative_index = index - len(words_list)
        if negative_index <= -2:
            proverbs.append(sentence)

        if word_2 < len(words_list) - 1:
            word_2 += 1

    if len(words_list) >= 1:
        if qualifier:
            last_sentence = f"And all for the want of a {qualifier} {words_list[0]}."
        else:
            last_sentence = f"And all for the want of a {words_list[0]}."
        proverbs.append(last_sentence)
    return proverbs
