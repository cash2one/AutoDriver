# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from framework.core import the,device,task


def main():
    the.android = device.android()

    _task = task.Task(the.android,False,100)
    device_run = device.RunTest(_task)
    device_run.start()


if __name__ == "__main__":
    main()

