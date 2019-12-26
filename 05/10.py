num = int(input('Enter your number:'))


def rec_foo(n):
    if n == 1:
        return 1
    else:
        return n + rec_foo(n - 1)


print((rec_foo(num)))
