def replace_char(some_str, ind, char):
    some_str = some_str[:int(ind)] + char + some_str[ind + 1:]
    print(some_str)


my_str = 'Hello World'
replace_char(my_str, 1, 'a')

print(my_str.replace(my_str[1], 'a'))
