def all_english_words():
    f = open('/usr/share/dict/words', 'r')
    for word in f:
        yield word.strip()


def filter_every_other(things):
    i = 0
    for thing in things:
        if i % 2 == 0:
            yield thing
        i += 1


class MyError(Exception):
    pass


def filter_longer(words, n):
    if not isinstance(n, int):
        return 'errore'
    if n <= 0:
        return 'errore 2'
    for word in words:
        if len(word) > n:
            yield word


def one_two_three():
    yield 1
    yield 2
    yield 3


def i_am_useless():
    # with open('generators.md', 'r') as f:
    #     f.write('ciao')
    f = open('generators.md', 'r')
    try:
        f.write('ciao')
    except OSError:
        return 1
    finally:
        f.close()

def sum_three_ints(a, b, c):
    a_b, error = sum_ints(a, b)
    if error:
        return error
    a_b_c, error = sum_ints(a_b, c)
    if error:
        return error
   return a_b_c


def sum_ints(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return None, 'error'
    return a + b, None
