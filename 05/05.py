some_str = 'Fvjsjk. VDFV, cefsd Vfdkf!'

spaces = some_str.split(' ')
big_chr = 0
small_chr = 0
punctuation = 0

for i in some_str:
    if 'a' <= i <= 'z':
        small_chr += 1
    elif 'A' <= i <= 'Z':
        big_chr += 1
    elif i in [',', '.', ':', ';', '!', '?']:
        punctuation += 1

print('spaces: {},'.format(len(spaces) - 1), end=' ')
print('lower: {}, upper: {}, punctuation: {}'.format(small_chr, big_chr, punctuation))
