from word2number.w2n import word_to_num


def foo(*args):
    sum_of_num = 0
    for i in range(len(args)):
        sum_of_num += word_to_num(args[i])
    print(sum_of_num)


foo('five', 'six', 'ten', 'one')
