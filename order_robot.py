# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import time
import threading
import xmlrpclib
from framework.core import device,idriver

class MonitorOrder(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
        host = idriver.xmlrpc_host()
        port = idriver.xmlrpc_port()
        self.xmlrpc = xmlrpclib.ServerProxy('http://%s:%s' % (host,int(port)))
        self.driver = device.Android('android.idriver.driver')
        self.driver.login()

    def run(self):
        while not self.thread_stop:
            if self.have_driver_action():
                #获取完状态订单状态后，恢复订单状态
                try:
                    self.xmlrpc.set_customer_action(False)
                    print 'modify server action'
                except xmlrpclib.Fault:
                    pass

                time.sleep(3)
                print 'start order'
                self.order()

            time.sleep(2)

    def have_driver_action(self):
        return self.xmlrpc.get_customer('action')

    def stop(self):
        self.thread_stop = True

    def order(self):
        self.driver.find_id('iv_head').click()


if __name__ == "__main__":
    mo = MonitorOrder()
    mo.start()