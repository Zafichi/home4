def foo(first_num, second_num, result):
    print(first_num, end=' ')
    print(second_num, end=' ')
    for i in range(result + 1):
        if first_num + second_num < result:
            next_num = first_num + second_num
            first_num = second_num
            second_num = next_num
            print(next_num, end=' ')
            if first_num + second_num == result:
                print(result)
                print('True')
                break
            elif first_num + second_num < result:
                continue
            print('\nFalse')


foo(3, 5, 53316291173)
