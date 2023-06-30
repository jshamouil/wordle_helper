from words import words_list


def in_yellow(let, i, word):
    return let == word[i] or let not in set(word[0:i] + word[i + 1:])


def calc(guess, output, words=None):

    if words is None:
        words = set(words_list)
    gray, out_words, in_words = set(), set(), set()
    yellow, green = [], []
    out = [int(i) for i in output.split(",")]
    for ind, let in enumerate(guess):
        if out[ind] == 3:
            gray.add(let)
        if out[ind] == 2:
            yellow.append((let, ind))
        if out[ind] == 1:
            green.append((let, ind))
    for let, i in yellow:
        if let in gray:
            gray.remove(let)
    for word in words:
        out_words.update({word for i in gray if i in word})
        out_words.update({word for let, i in yellow if in_yellow(let, i, word)})
        if all([let == word[i] for let, i in green]):
            in_words.add(word)
    words = (words.difference(out_words)).intersection(in_words)
    return words
