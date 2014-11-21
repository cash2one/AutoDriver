# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import subprocess
import threading
#from framework.core import the,device,task,idriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def main():
    pass
    # _task = task.Task(PATH('./testcase/'),2)
    # device_run = device.RunTest(_task)
    # device_run.start()

def run_ium(port):
    p1 = subprocess.Popen('appium --port %s' % port, stdout=subprocess.PIPE, shell=True)
    p1.stdout.read()

class MonitorOrder(threading.Thread):

    def __init__(self,port=4723):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        p1 = subprocess.Popen('appium --port %s' % self.port, stdout=subprocess.PIPE, shell=True)
        p1.stdout.read()


if __name__ == "__main__":
    # #main()
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
    #     print 'gegwwwwww'
    #     time.sleep(2)

    # p1 = subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
    # p1.stdout.read()
    #
    # p2 = subprocess.Popen('appium --port %s' % 4726, stdout=subprocess.PIPE, shell=True)
    # p2.stdout.read()
    # from framework.core import the
    # ps = the.project_settings
    #
    # # mo = MonitorOrder(4723)
    # # mo.start()
    # # print 'fff'
    # aaa=[4723,4725]
    # for a in aaa:
    #     print a
    #     mo = MonitorOrder(a)
    #     mo.start()
    #     print mo.ident
    #     time.sleep(5)
    #
    # class DemoOne():
    #     def __init__(self,word):
    #         self.word = word
    #
    #     def do1(self):
    #         print self.word
    #
    #     def do2(self):
    #         return 'abcdddd'
    #
    # class DemoTwo():
    #     def __init__(self,inst=None):
    #         self.inst = inst('aad')
    #
    #     def dt1(self):
    #         return self.inst
    #
    # dt = DemoTwo(DemoOne)
    #
    # dt.dt1().do1()
    # print dt.dt1().do2()
    from framework.util import str

    #dd = str.to_datetime(u'2014-11-12 15:51:52')

    import string
    print str.to_long('1302203.332')



    # for p in ps:
    #     port_ = 0
    #     try:
    #         remote_port = ps[p]['remote_port']
    #         port_ = int(remote_port)
    #     except KeyError:
    #         port_ = 0
    #
    #     if port_!=0:
    #         mo = MonitorOrder(port_)
    #         mo.start()