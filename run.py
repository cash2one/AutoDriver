# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import subprocess
from framework.core import the,device,task,idriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def main():

    _task = task.Task(PATH('./testcase/'),2)
    device_run = device.RunTest(_task)
    device_run.start()


if __name__ == "__main__":
    #main()
    p = subprocess.Popen('appium --port 4725', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    #print p.stdout.readlines()
    for line in p.stdout.readlines():
        print line,
    p.wait()
