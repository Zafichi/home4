def rec_lst(lst):
    if len(lst) == 0:
        return 1
    else:
        return rec_lst(lst[:-1]) * lst[-1]


some_lst = [42, 72, 113]

print(rec_lst(some_lst))
