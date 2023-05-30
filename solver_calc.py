"""solver class"""

from words import words_list

def in_yellow(let, i, word):
    """solver function"""
    return let == word[i] or let not in set(word[0:i] + word[i+1:])

def calc():
    """solver function"""

    words = set(words_list)

    guess = "shiny"
    output = "1,1,1,3,3"


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
    for word in words:
        out_words.update({word for i in gray if i in word})
        out_words.update({word for l, i in yellow if in_yellow(l, i, word)})
        if all([l == word[i] for l, i in green]):
            in_words.add(word)
    words = (words.difference(out_words)).intersection(in_words)

calc()
