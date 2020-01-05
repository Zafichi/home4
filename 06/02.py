import re


def first_three_char(some_str):
    lst = some_str.split()
    for i in lst:
        if len(i) == 1:
            print(i + '  ', end=' ')
        elif len(i) == 2:
            print(i + ' ', end=' ')
        else:
            print(i[:3], end=' ')


first_three_char('fjsdfhj fhsfhh trjtb nvd vf f jfi klm g,')
