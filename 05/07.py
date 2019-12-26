import math

num = int(input('Enter your number:'))

if num < 2:
    print('Number might be more than one!')
    quit()
elif num == 2:
    print('This is a prime number)')
    quit()

divider = 2
limit = int(math.sqrt(num))

while divider <= limit:
    if num % divider == 0:
        print('This is a compound number(')
        quit()
    divider += 1

print('This is a prime number)')
