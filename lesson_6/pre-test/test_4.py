# coding: utf-8

trans = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(english):
    swedish = []
    for word in english.split():
        if word in trans:
            swedish.append(trans[word])
        else:
            swedish.append(word)
    return ' '.join(swedish)


def translate_2(english):
    swedish = ''
    for word in english.split():
        if word in trans:
            swedish += trans[word] + ' '
    return swedish[:-1]
