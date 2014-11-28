# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import time
import threading
import xmlrpclib
from framework.core import device,idriver_android

class MonitorOrder(threading.Thread):
    '''
    通常order_robot 和 order_server 在一台机器上运行。
    参数都读取自根目录的config.ini [xmlrpc]
    '''

    def __init__(self,device_app):
        threading.Thread.__init__(self)
        self.thread_stop = False
        host = device.xmlrpc_host()
        port = device.xmlrpc_port()
        self.xmlrpc = xmlrpclib.ServerProxy('http://%s:%s' % (host,int(port)))
        #self.driver = device.app('idriver.android.customer')
        self.driver = device_app
        #idriver.login_driver()

    def run(self):
        while not self.thread_stop:
            if self.have_order():
                #获取完状态订单状态后，恢复订单状态
                try:
                    self.xmlrpc.set_customer(False,'')
                    print 'modify server action'
                except xmlrpclib.Fault:
                    pass

                time.sleep(5)
                print 'start order'
                self.place_order()

            time.sleep(2)

    def have_order(self):
        return self.xmlrpc.get_customer('action')

    def stop(self):
        self.thread_stop = True

    def place_order(self):
        '''
        下订单
        :return:
        '''
        contact_phone = self.driver.configs['contact_phone']

        idriver_android.login_customer(self.driver)
        self.driver.find_id('rb_order').click()

        time.sleep(1)
        self.driver.clear_text('tv_phone')
        self.driver.find_id('tv_phone').send_keys(contact_phone)

        self.driver.find_id('tv_address').click()
        self.driver.wait_switch('.MainActivity')

        self.driver.find_ids('tv_currentposition')[0].click()
        self.driver.wait_switch('.OrderAdressActivity')

        self.driver.find_id('bt_order').click()


    def receive_oder(self):
        '''
        接订单
        :return:
        '''
        pass


if __name__ == "__main__":
    # da = device.app('idriver.android.customer')
    # mo = MonitorOrder(da)
    # mo.start()
    from framework.core import idriver_android
    idriver_android.client()