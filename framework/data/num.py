# coding=utf-8
__author__ = 'Administrator'

import time

# 自增长编号 10000
def no(last_no):
    t = time.strftime('%y%m%d', time.localtime(time.time()))
    if cmp(t, str(last_no)[:6]) == -1:
        for i in range(10000):
            filename = "%s%04d" % (t, i)
            return int(filename)
    else:
        return last_no + 1