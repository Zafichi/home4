lst = [[3, 5, 8], [5, 8, 10], [1, 2], [2, 13, 9]]
lst = sorted(lst, key=lambda x: sum(x), reverse=True)
print(lst)
