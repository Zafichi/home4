def how_much_time(func):
    import time

    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print('Time has passed: {}'.format(end - start))
        return res
    return wrapper


@how_much_time
def foo(*args):
    tup = sorted(args)
    print(tup[-2])


foo(2, 5, 1, 7, 12)
