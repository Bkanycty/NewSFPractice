from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg,
                                             int):  # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(
            f'Нельзя умножить {type(value)} на {type(arg)}')  # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку


@register.filter(name='censor')
def censor(value):
    obscene_words = ['хуй', 'пизд', 'еба', 'ебу', 'бля', 'Текст']
    value_censored = []
    for word in value.split():
        if word in obscene_words:
            value_censored.append(f'{word[0]}{"*"*(len(word)-2)}{word[-1]}')
        else:
            value_censored.append(word)
    return " ".join(value_censored)
