def split_dot(phrase: str):
    word_group = phrase.split()
    result = list()
    dot = list()
    no_dot = list()

    for word in word_group:
        dot.append(word)
        no_dot.append(word)

        if "." in word:
            result.append(" ".join(dot))
            dot.clear()
            no_dot.clear()

    result.append(" ".join(no_dot))
    return result
