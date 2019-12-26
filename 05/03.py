from word2number.w2n import word_to_num

dict_of_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}


def fun(*args):
    sum_of_num = 0
    for i in args:
        sum_of_num += dict_of_num[i]
    print(sum_of_num)


def foo(*args):
    sum_of_num = 0
    for i in range(len(args)):
        sum_of_num += word_to_num(args[i])
    print(sum_of_num)


foo('five', 'six', 'ten', 'one', 'two')
fun('five', 'six', 'ten', 'one', 'two')
