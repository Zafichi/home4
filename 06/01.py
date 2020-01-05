import re


def first_word(some_str):
    print(list(some_str .split())[0])


first_word('Hello world and space')


def reg_first_word(some_str):
    result = re.match(r'^\w+', some_str)
    print(result.group(0))


reg_first_word('Helloo world and space')
