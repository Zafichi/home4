from itertools import groupby

lst = [19, 12, 4, 12, 7, 9, 5, 8, 3, 17, 8, 19, 12, 3, 6, 15, 15, 16, 11, 13, 19, 16, 11, 12, 20,
       2, 16, 7, 15, 2, 6, 15, 17, 15, 19, 4, 13, 14, 6, 5, 12, 2, 20, 7, 19, 4, 15, 16, 7, 20]

lst.sort(reverse=True)
new_lst = [i for i, _ in groupby(lst)]
print(new_lst)
