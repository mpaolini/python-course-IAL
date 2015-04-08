# Exceptions

Write a generator that returns all positive integers and accepts a value sent with
`.send()` as the step.


    >>> import exception_exercise
    >>> ints = exception_exercise.get_ints()
    >>> next(ints)
    1
    >>> next(ints)
    2
    >>> ints.send(3)
    5
    >>> ints.send(-2)
    Traceback (most recent call last):
        ...
    ValueError: step must be positive
    >>> ints.send(1)
    Traceback (most recent call last):
        ...
    StopIteration
