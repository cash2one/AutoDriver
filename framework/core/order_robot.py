# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import time
import sys
import threading
import ConfigParser
import xmlrpclib
import app

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def readConfig(opt):
    path_str = PATH('../../config.ini')
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get('xmlrpc',opt)

def get_host():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(host_name)

class OrderServer():
    '''
    订单机器人服务器端
    '''
    def __init__(self):
        self.driver_info = {'driver_no':'14009','action':False}
        self.customer_info = {'user_name':'','action':False,'req':False}

    def get_driver(self):
        return self.driver_info

    def get_customer(self):
        return self.customer_info

    def set_driver_action(self,bol):
        try:
            self.driver_info['action'] = bol
        except KeyError:
            pass

    def set_customer_action(self,bol):
        try:
            self.customer_info['action'] = bol
        except KeyError:
            pass

    # def request(self,server_host,server_port):
    #     s = self.xml_server(server_host,server_port)
    #     s.set_value('req',True)

    def reply(self,bol):
        host,port = get_host()
        s = xmlrpclib.ServerProxy('http://%s:%s' % (host,port))
        s.set_value('req',True)

class MonitorOrder(threading.Thread):

    def __init__(self,port):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.sev = xmlrpclib.ServerProxy('http://%s:%s' % (get_host(),int(port)))
        self.driver = app.Android('')
        self.is_order = False

    def run(self):
        while not self.thread_stop:

            if self.is_start():
                self.is_order = True
                print self.sev.get_customer()

            time.sleep(1)

            # if self.is_order:
            #     self.order()
            #     self.is_order = False

    def is_start(self):
        return self.sev.get_value('action')

    def stop(self):
        self.thread_stop = True

    def order(self):
        print 'autotoot'
        # self.driver.switch_to_home()
        #
        # current_activity = self.driver.current_activity()
        # self.driver.find_id('iv_head').click()
        #
        # self.driver.switch_finish(current_activity)
        #
        # title_text = self.driver.find_id('tv_title_text').text



def print_help():
    print 'python order_robot.py 1234'

if __name__ == "__main__":
    args = sys.argv

    if len(args) > 1:
        mo = MonitorOrder(args[1])
        mo.start()
    else:
        print_help()