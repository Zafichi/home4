import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text_to_find', nargs='*')
parser.add_argument('-p', '--path')

file_name = input('Enter name of the file: ')
if parser.parse_args().path is not None:
    file_name = os.path.join(parser.parse_args().path, file_name)

if os.path.isfile(file_name):
    f = open(file_name)
    str_find = ' '.join(parser.parse_args().text_to_find)
    counter_of_lines = 1
    # counter_of_str = 0
    for line in f:
        if str_find.lower() in line.lower():
            print('\'{}\', path to the file \'{}\', number of the string: {}'.format(line, os.path.abspath(file_name),
                                                                                     counter_of_lines))
            # for i in line:
            #     if i.lower() in line.lower():
            #         counter_of_str += 1
        counter_of_lines += 1
    # print(counter_of_str)
    f.close()
else:
    print('No such file!')
