import datetime
import numpy


def working_days_spl(y1, m1, d1, y2, m2, d2):
    start_date = datetime.date(y1, m1, d1)
    end_date = datetime.date(y2, m2, d2)
    print('Working days during this period:', numpy.busday_count(start_date, end_date))


def working_days(first_str, second_str):
    first_str_spl = first_str.split('_')
    second_str_spl = second_str.split('_')
    working_days_spl(int(first_str_spl[0]), int(first_str_spl[1]), int(first_str_spl[2]),
                     int(second_str_spl[0]), int(second_str_spl[1]), int(second_str_spl[2]) + 1)


first_string, second_string = '2019_12_2', '2019_12_9'

working_days(first_string, second_string)
