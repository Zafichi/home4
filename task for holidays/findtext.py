import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text_to_find', nargs='*')
parser.add_argument('-p', '--path')

counter_of_str = 0
files = os.listdir(os.getcwd())
for file_name in files:
    if parser.parse_args().path is not None:
        file_name = os.path.join(parser.parse_args().path, file_name)

    if os.path.isfile(file_name):
        f = open(file_name)
        str_find = ' '.join(parser.parse_args().text_to_find)
        counter_of_lines = 1
        for line in f:
            if str_find.lower() in line.lower() and counter_of_str <= 100:
                print('Match string: \'{}\', path to the file \'{}\', string number: {}\n'
                      .format(line, os.path.abspath(file_name), counter_of_lines))
                counter_of_str += 1
            counter_of_lines += 1
        f.close()
