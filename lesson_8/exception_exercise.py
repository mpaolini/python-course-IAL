def get_ints():
    n = 1
    while True:
        step = yield n
        if step is None:
            step = 1
        if step < 0:
            raise ValueError('step must be positive')
        n += step
