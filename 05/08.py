
def foo(strr):
    if strr == strr[::-1]:
        print(True)
    else:
        print(False)


some_str1 = 'abba'
some_str2 = 'Hello'
some_str3 = 'radar'

foo(some_str1)
foo(some_str2)
foo(some_str3)
