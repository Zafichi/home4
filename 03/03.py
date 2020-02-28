def foo(num):
    first_num = str(num)
    second_num = str(num) * 2
    third_num = str(num) * 3
    fourth_num = str(num) * 4
    print(first_num, '+', second_num, '-', third_num, '*', fourth_num, end=' = ')
    print(int(first_num) + int(second_num) - int(third_num) * int(fourth_num))


foo(input('Enter the number: '))
foo(5)

