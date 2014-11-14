# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import datetime,string,re

def to_datetime(str_time):
    return datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')

def isFloat(str_number):
    pattern = re.compile(r'^\d+\.?\d+$|^\d+$')
    match = pattern.match(str_number)
    if match:
        return True
    else:
        return False

def isNumber(str_number):
    pattern = re.compile(r'^[(-?\d+\.\d+)|(-?\d+)|(-?\.\d+)]+$')
    match = pattern.match(str_number)
    if match:
        return True
    else:
        return False

def longToInt(value):
    if value > 2147483647:
        return (value & (2 ** 31 - 1))
    else:
        return value

def to_long(str_number):
    if not isNumber(str_number):
        return None

    if isFloat(str_number):
        return long(string.atof(str_number))
    else:
        return string.atol(str_number)



# def to_int(str_number):
#     if not isNumber(str_number):
#         return None
#
#     if isFloat(str_number):
#         return int(string.atof(str_number))
#     else:
#         return longToInt(str_number)






