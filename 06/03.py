import re

lst = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com',
       'seemant@yahoo.com', 'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca',
       'joehall@msn.com', 'ilikered@optonline.net']


def find_dom(some_lst):
    new_lst = []
    for i in some_lst:
        start_from = i.find('@')
        end_on = i.rfind('.')
        new_lst.append(i[start_from: end_on])
    print(new_lst)


find_dom(lst)

result = re.findall(r'@\w+', ''.join(lst))
print(result)
