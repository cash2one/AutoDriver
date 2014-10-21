# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import subprocess
#from framework.core import the,device,task,idriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def main():
    pass
    # _task = task.Task(PATH('./testcase/'),2)
    # device_run = device.RunTest(_task)
    # device_run.start()


if __name__ == "__main__":
    #main()
    p = subprocess.Popen('ls --help', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #print p.stdout.readlines()
    for line in p.stdout.readlines():
        print line,
    #p.wait()

    print 'continue'
