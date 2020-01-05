def swap_case(some_str):
    swap_str = ''
    for i in some_str:
        if i.isupper():
            swap_str += i.lower()
        else:
            swap_str += i.upper()
    print(swap_str)


my_str = 'Hello World'
swap_case(my_str)

print(my_str.swapcase())
