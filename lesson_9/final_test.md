## test_1.py

Please implement a function that returns the middle item of a list. If
the list is empty, return `None`.

If the list has even numbers of entries, return the first item closest to the
center

    >>> import test_1
    >>> l = [1, 3, 5]
    >>> test_1.get_middle(l)
    3
    >>> test_1.get_middle([2, 5, 9, 8])
    5
    >>> test_1.get_middle([]) == None
    True


## test_2.py

    >>> import test_2

Write a function get_occurrences() that takes a list of words and returns the
number of words that contains the word specified.

    >>> test_2.get_occurrences(['cat', 'dog', 'penguin'], 'cat')
    1
    >>> test_2.get_occurrences(['cat', 'cat', 'cat', 'dog'], 'cat')
    3
    >>> test_2.get_occurrences([], 'hey')
    0


## test_3.py

    >>> import test_3

Write a function that outputs all lines of a file that are longer than a certain
value.

It accepts two arguments: the name of the origin file and an integer

It returns a generator that yields one line at a time.

    >>> lines = test_3.grep_lines('test_3_helper.txt', 4)
    >>> next(lines)
    'penguin'
    >>> next(lines)
    'hey Joe!'
    >>> next(lines)
    'catamaran'
    >>> next(lines)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> lines = test_3.grep_lines('test_3_helper.txt', 7)
    >>> next(lines)
    'hey Joe!'
    >>> next(lines)
    'catamaran'
    >>> next(lines)
    Traceback (most recent call last):
        ...
    StopIteration


## test_4.py

    >>> import test_4

Write a function that computes the number of occurences of a set of control
words in a phrase.

It accepts a phrase (as a string) and a list of words.

It returns a dictionary with all check words as keys and their occurrence
as value.


    >>> test_4.count_words('merry christmas', ['merry']) == {'merry': 1}
    True
    >>> test_4.count_words('white cat and black cat', ['cat', 'hat']) == {'cat': 2, 'hat': 0}
    True


## test_5.py


    >>> import test_5

Write a function that sorts words passed in as list and returns a single string
with each word in a line (separated by newline)


    >>> test_5.sort_words_nl(['one', 'two', 'three'])
    'one\nthree\ntwo'
    >>> test_5.sort_words_nl(['penguin', 'cat'])
    'cat\npenguin'


## test_6.py

Write a function that multiplies numbers. Numbers can be passed as variable
number of args.

    >>> import test_6
    >>> test_6.multiply(1, 2)
    2
    >>> test_6.multiply(1, 2, 3)
    6


## test_7.py

The remote endpoint http://private-bb81a-ialpython.apiary-mock.com/workstations
keeps the status of all workstation in the laboratory.

Implement python client that queries the remote resource and returns all the
names of the workstations that are misconfigured and have the same ip address.

Output sorting is not relevant.

    >>> import test_7
    >>> names = test_7.get_misconfigured()
    >>> sorted(names)
    ['julia', 'nik']
