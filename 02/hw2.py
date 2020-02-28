# 1
try:
    first_num = float(input('Enter first number:'))
    second_num = float(input('Enter second number:'))
    sum_of_nums = first_num + second_num
    difference = first_num - second_num
    print(int(sum_of_nums))
    print(difference)
    print(sum_of_nums)
except ValueError as n:
    print("Exception, ", n)
else:
    print('Ok')


# 2
def num(value):
    if value % 2 == 0 and 2 <= value <= 27:
        print("In first range")
    elif value % 2 != 0 and 29 <= value <= 53:
        print("In second range")
    elif value % 2 == 0:
        print("Odd")
    else:
        print("It's something")


num(int(input("Enter number: ")))


# 3
def answer(first_value, second_value):
    print(int(first_value / second_value))
    print(first_value / second_value)


first_num = float(input('Enter first number:'))
second_num = float(input('Enter second number:'))

answer(first_num, second_num)

# 4
my_str = 'Going through the forest is my favourite part of the walk. My dog Benji loves it too. I\'m Grace. ' \
           'I live on a farm with my parents and I take Benji for a walk most days after school. While Benji\'s ' \
           'playing, I stop to take a photo of a butterfly. I\'m thinking about posting it on Facebook, but then ' \
           'I hear Benji barking. He\'s jumping and running around a boy. The poor boy looks worried. \'Benji, stop! ' \
           'Come here!\' I call and throw him his ball. I\'m about to say sorry to the boy, but he\'s gone.'


def str_in_column(some_str, max_len):
    new_str = '   '
    count = 0
    for i in some_str.split():
        count += len(i)
        if count > max_len:
            new_str += '\n\t'
            count = len(i)
        elif new_str != '':
            new_str += ' '
            count += 1
        new_str += i
    print(new_str)


str_in_column(my_str, 20)


# 5
def find_max(num_of_results, input_lst):
    for i in input_lst:
        if type(i) == str:
            input_lst.remove(i)
    input_lst.sort()
    input_lst.reverse()
    print(input_lst[0:num_of_results])


lst = [20, 58, 9, 23, 62, 'hi', 46, 48, 125.23, 55, 95, 68, 2, 2, 50, 'list', 76, 14, 92, 12, 71, 12, 30]
find_max(int(input('How much results do you want: ')), lst)


# 6
import math


def square_of_circle(r):
    s = (r**2) * math.pi
    print('Square of circle is: ', s)


square_of_circle(float(input('Enter radius of circle: ')))


# 7
def lo_rew(first_str, second_str):
    print(second_str.lower()[::-1], first_str.lower()[::-1])


lo_rew("Hello", 'World')


# 8
def list_of_one(lst_of_nums):
    while len(lst_of_nums) != 1:
        if len(lst_of_nums) > 3 and len(lst_of_nums) % 2 == 0:
            del lst_of_nums[1::2]
        elif len(lst_of_nums) > 3 and len(lst_of_nums) % 2 != 0:
            del lst_of_nums[1::2]
            lst_of_nums.pop(0)
        elif len(lst_of_nums) == 3:
            lst_of_nums.pop(1)
            lst_of_nums.pop(0)
        elif len(lst_of_nums) == 2:
            lst_of_nums.pop()
        print(lst_of_nums)


lst = [1, 2, 3, 4, 5, 6, 7, 8]
list_of_one(lst)
