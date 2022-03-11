def censor(value):
    obscene_words = ['хуй', 'пизд', 'еба', 'ебу', 'бля', 'стат']
    value_censored = []
    for word in value.split():
        for i in obscene_words:
            if i in word:
                value_censored.append(f'{word[0]}*{word[-1]}')
                break
            else:
                value_censored.append(word)
    return " ".join(value_censored)