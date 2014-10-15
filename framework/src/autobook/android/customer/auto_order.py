# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import sys
import threading
import ConfigParser
import xmlrpclib
from framework.core import extend

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def readConfig(selections,opt):
    path_str = PATH('./config.ini')
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get(selections,opt)

def get_host():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(host_name)

class MonitorOrder(threading.Thread):

    def __init__(self,port):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.sev = xmlrpclib.ServerProxy('http://%s:%s' % (get_host(),int(port)))
        self.driver = extend.Android()
        self.is_order = False

    def run(self):
        while not self.thread_stop:

            if self.is_start():
                self.is_order = True
                self.set_customer(False)

            if self.is_order:
                self.order()
                self.is_order = False

    def is_start(self):
        return self.sev.get_value('start')

    def stop(self):
        self.thread_stop = True

    def order(self):
        self.driver.switch_to_home()

        current_activity = self.driver.current_activity()
        self.driver.find_id('iv_head').click()

        self.driver.switch_finish(current_activity)

        title_text = self.driver.find_id('tv_title_text').text



def print_help():
    print 'python auto_order.py 1234'

if __name__ == "__main__":
    args = sys.argv

    if len(args) > 1:
        mo = MonitorOrder(args[1])
        mo.start()
    else:
        print_help()