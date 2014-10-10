# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.core import the,device,task

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def main():

    _task = task.Task(PATH('./testcase/'),2)
    device_run = device.RunTest(_task)
    device_run.start()


if __name__ == "__main__":
    main()

