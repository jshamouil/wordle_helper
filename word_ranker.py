import pandas as pd

def ranker(words_remaining_1):
    d = {'letters': ["e", "a", "r", "i", "o", "t", "n", "s", "l", "c", "u", "d", "p", "m", "h", "g", "b", "f", "y", "w", "k", "v", "x", "z", "j", "q"],
        'points': [56.88, 43.31, 38.64, 38.45, 36.51, 35.43, 33.92, 29.23, 27.98, 23.13, 18.51, 17.25, 16.14, 15.36, 15.31, 12.59, 10.56, 9.24, 9.06, 6.57, 5.61, 5.13, 1.48, 1.39, 1, 1]
    }
    point_table = pd.DataFrame(data=d)

    scores = []
    for i in words_remaining_1:
        list_word = set(list(i))
        score = round(sum([float(point_table[point_table["letters"] == j]["points"]) for j in list_word]), 2)
        scores.append(score)

    scored_words = pd.DataFrame(data={"words": words_remaining_1, "scores": scores})
    scored_words = scored_words.sort_values(by="scores", ascending=False)
    scored_words = list(scored_words["words"])
    top_10 = ", ".join(scored_words)
    return top_10
