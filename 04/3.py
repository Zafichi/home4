from collections import Counter

str1 = 'bhfvsjgwt'
str2 = 'efuiwo .;'
str3 = 'dqwuei vsdifvuh.'
str4 = ' vkdf ff., vfo'
str5 = 'fsfksj'
str6 = 'vdfgbd'
str7 = 'gdfg'
str8 = 'kut'
str9 = 'bgdf'
str10 = 'vwrbbr'

big_ten_str = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10

lst = [i for i in big_ten_str]
dict_of_chars = Counter(lst).most_common(1)
print(dict_of_chars)
