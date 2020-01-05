def replace_spaces(some_str):
    str_without_spaces = ''
    for i in some_str:
        if i == ' ':
            str_without_spaces += '-'
        else:
            str_without_spaces += i
    print(str_without_spaces)


my_str = 'Hello World!You are amazing!'
replace_spaces(my_str)

print(my_str.replace(' ', '-'))
