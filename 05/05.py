some_str = 'Fvjsjk VDFV cefsd Vfdkf!'

spaces = some_str.split(' ')
big_chr = 0
small_chr = 0
znaki = 0

for i in some_str:
    if 'a' <= i <= 'z':
        small_chr += 1
    elif 'A' <= i <= 'Z':
        big_chr += 1
    else:
        znaki += 1

print(len(spaces))
print(small_chr, big_chr, znaki)
