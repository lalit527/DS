def word_split(phrase, words, output = None):
    if output is None:
        output = []

    for word in words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], words, output)

    return output




print(word_split('themanran',['the','ran','man']))