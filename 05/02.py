def fun(*args, **kwargs):
    for i in kwargs.values():
        if i == args[0]:
            print(True)
            break
    else:
        print(False)


fun(5, foo=5, bar=9)
