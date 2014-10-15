__author__ = 'guguohai@pathbook.com.cn'

import os
import ConfigParser
import re
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

driver_info = {'driver_no':'14009','action':False}
customer_info = {'user_name':'','action':False,'req':False}


def isHost(value):
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True #match.group()
    else:
        return False


class OrderServer():
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

def readConfig(selections,opt):
    path_str = PATH('./config.ini')
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get(selections,opt)

def get_host():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    host_addr = socket.gethostbyname(host_name)
    port = readConfig('server','port')
    return host_addr,port

def register():
    host_addr,port = get_host()

    server = SimpleXMLRPCServer((host_addr, int(port)))
    server.register_instance(OrderServer())
    server.serve_forever()