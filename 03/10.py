lst1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
lst2 = [5, 8, 13, 42]

new_lst = []
for i in lst1:
    if lst1[i] == lst2[0]:
        for j in lst2:
            print(j)
            ind = i
            if lst2[j] == lst1[ind]:
                new_lst.append(j)
                ind += 1
    if len(new_lst) == len(lst2):
        break

if new_lst == lst2:
    print('True')
else:
    print('False')
print(new_lst)
print(len(lst2))
