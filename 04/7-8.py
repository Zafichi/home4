# 7

from random import choice
import random
import string

lst = []
rnd = random.randint(1, 4)
n = int(input('Enter how much string do you wont:'))

for i in range(n):
    lst.append(''.join(choice(string.ascii_letters) for j in range(rnd)))

print('Out from 7th task {}:'.format(lst))

# 8

rev_lst = []
for i in lst:
    rev_lst.append(i[::-1])
print('Out from 8th task {}:'.format(sorted(rev_lst, key=str.lower)))
