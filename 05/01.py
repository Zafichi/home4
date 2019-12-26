def foo(*args):
    tup = sorted(args)
    print(tup[-2])


foo(2, 5, 1, 7, 13)
