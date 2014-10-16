# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import ConfigParser
import re
from SimpleXMLRPCServer import SimpleXMLRPCServer



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# driver_info = {'driver_no':'14009','action':False}
# customer_info = {'user_name':'','action':False,'req':False}
#
#
# def isHost(value):
#     pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
#     match = pattern.match(value)
#     if match:
#         return True #match.group()
#     else:
#         return False

def readConfig(opt):
    path_str = PATH('../../config.ini')
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get('xmlrpc',opt)

def get_host():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    host_addr = socket.gethostbyname(host_name)
    return host_addr

def register():
    import order_robot
    inst = order_robot.OrderServer()

    host_addr = get_host()
    port = int(readConfig('port'))

    server = SimpleXMLRPCServer((host_addr, port))
    server.register_instance(inst)
    server.serve_forever()




if __name__ == "__main__":
    register()