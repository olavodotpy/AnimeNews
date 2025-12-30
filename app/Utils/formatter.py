# 🙈

def formatter_text(phrase: str) -> list:
    word_group = phrase.split()
    result = []
    dot = []
    no_dot = []

    for word in word_group:
        dot.append(word)
        no_dot.append(word)

        try:
            if ("." in word and word_group[word_group.index(word) + 1] != "("
                and word_group[word_group.index(word) + 1] != ")."
                and word_group[word_group.index(word) + 1] != ")"
            ):
                result.append(" ".join(dot))
                dot.clear()
                no_dot.clear()
        except:
            return phrase

    result.append(" ".join(no_dot))
    return result
