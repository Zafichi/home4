def calculate_chars(some_str):
    some_str = some_str.lower()
    counter = []
    num = []
    for i in range(len(some_str)):
        count = 0
        if some_str[i] not in counter:
            counter += some_str[i]
            for j in range(len(some_str)):
                if some_str[j] == some_str[i]:
                    count += 1
            num.append(count)
        else:
            continue
    chars = dict(zip(counter, num))
    print(chars)


my_str = 'Hello Big Brother!)))'
calculate_chars(my_str)


