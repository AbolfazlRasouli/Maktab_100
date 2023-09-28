from datetime import datetime as dt
from jdatetime import datetime as jdt


def datetime_distance(datetime1, datetime2):
    """ Calculate distance between of two datetime """
    seconds_distance = datetime2.timestamp() - datetime1.timestamp()
    print()
    return f'{datetime2.timestamp()} - {datetime1.timestamp()} = {abs(seconds_distance)}'
        
def format_changer(datetime1, datetime2, pf):
    """ chnage string to datetime object """
    datetime1 = dt.strptime(datetime1, pf)
    datetime2 = dt.strptime(datetime2, pf)
    return datetime1, datetime2 

def cal_leap_years(datetime1, datetime2):
    """ Calculate number of leap years between two years date """
    min_date = min(datetime1.year, datetime2.year)
    max_date = max(datetime1.year, datetime2.year)
    
    leap_years = 0
    for year in range(min_date, max_date + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years += 1
    
    return leap_years
            
def change_to_ShamsiDate(datetime1, datetime2):
    """ Change Gregorian datetime obj to Shamsi datetime obj """
    jdatetime1 = jdt.fromgregorian(datetime=datetime1)
    jdatetime2 = jdt.fromgregorian(datetime=datetime2)
    jdatetime1_str = jdatetime1.strftime("%Y/%m/%d %H:%M:%S")
    jdatetime2_str = jdatetime2.strftime("%Y/%m/%d %H:%M:%S")
    
    return ('first datetime : {}\n'
            'second datetime : {}').format(jdatetime1_str, jdatetime2_str)
    
# datetime1_str = input('first date & time: 2000/00/00 00:00:00')
# datetime2_str = input('second date & time: 2000/00/00 00:00:00')
datetime1_str = '2020/11/02 20:30:11'
datetime2_str = '2002/07/19 17:55:40'
pattern_format = "%Y/%m/%d %H:%M:%S"

try:
    datetime1_obj, datetime2_obj = format_changer(datetime1_str, datetime2_str, pattern_format)

    print(datetime_distance(datetime1_obj, datetime2_obj))
    print(cal_leap_years(datetime1_obj, datetime2_obj))
    print(change_to_ShamsiDate(datetime1_obj, datetime2_obj))
except ValueError as e:
    print(e)
except Exception as E:
    print(E)