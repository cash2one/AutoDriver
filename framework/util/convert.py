# coding=utf-8
__author__ = 'guguohai@outlook.com'

import time


def utc_to_local(utc_str):
    # t='2014-12-05T15:03:10.000+0800'
    #将时间字符串根据指定的格式化符转换成struct_time
    time_s = time.strptime(utc_str, "%Y-%m-%dT%H:%M:%S.%f+0800")

    #将一个struct_time转化为时间戳
    #time_stamp = time.mktime(time_s)
    #timeArray = time.localtime(time_stamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_s)