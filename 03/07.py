lst = [1, 1, 2, 1, 2, 1, 2, 3, 3, 2, 2]
max_count = 0
for i in lst:
    if lst.count(lst[lst.index(i)]) > max_count:
        max_count = lst.count(lst[lst.index(i)])
print(max_count)
