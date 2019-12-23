import random
import bisect

lst = [random.randint(1, 20) for x in range(random.randint(5, 10))]
lst.sort()
print(lst)
for i in range(5):
    rnd = random.randint(1, 20)
    bisect.insort(lst, rnd)
    print('{0} -> {1}'.format(rnd, lst))
