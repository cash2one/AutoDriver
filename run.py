# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
from framework.core import task

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def main():
    case_list = [
        {'cases': {'test_customer_allfinishOrder': 5, 'test_customer_callServer_xgh': 3}, 'status': 0,
         'path': 'testcase/AutobookClient/customer'},
        {'cases': {'test_driver_cmEarnings_zc': 3, 'test_driver_completeOrder_info__zc': 2}, 'status': 0,
         'path': 'testcase/AutobookClient/driver'}
    ]

    task_list = []
    for c in case_list:
        t = task.Task(c)
        task_list.append(t)

    runner = task.TestRunner(task_list)
    runner.start()


if __name__ == "__main__":
    main()
    # import time
    # from framework.core import device
    #
    # dr = device.RunAppium(4725)
    # dr.start()
    # #
    # # p1 = subprocess.Popen('appium --port 4725',stdout=subprocess.PIPE,shell=True)
    # # os.popen('appium --port 4725')
    # #
    # # aa = p1.stdout.read()
    # # if 'debug: Non-default server args: {"port":4725}' in aa:
    #
    #
    # while 1:
    # print 'gegwwwwww'
    #     time.sleep(2)

    # p1 = subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
    # p1.stdout.read()
    #
    # p2 = subprocess.Popen('appium --port %s' % 4726, stdout=subprocess.PIPE, shell=True)
    # p2.stdout.read()
