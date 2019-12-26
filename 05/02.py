def fun(*args, **kwargs):
    for key in kwargs.keys():
        if kwargs[key] == args:
            print(True)
        else:
            print(False)


fun(5, foo=5, bar=8)
