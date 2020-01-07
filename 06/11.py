def roman_to_int(roman_num):
    roman_num = roman_num.upper()
    dict_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dict_big_nums = {('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800}
    result = 0
    prev_num = None
    for num in roman_num:
        if prev_num and dict_nums[prev_num] < dict_nums[num]:
            result += dict_big_nums[(prev_num, num)]
        else:
            result += dict_nums[num]
        prev_num = num
    print(result)


roman_to_int('IX')
roman_to_int('xiv')
roman_to_int('xlV')
roman_to_int('mMxX')
roman_to_int('DxxIx')

