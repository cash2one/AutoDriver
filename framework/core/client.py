# coding=utf-8
__author__ = 'Administrator'

import sys
import re
import xmlrpclib

def request_order(host,bol):
    '''
    司机端用来通知用户端 发送订单的请求
    :param host:
    :param bol:
    :return:
    '''
    s = xmlrpclib.ServerProxy('http://'+host)
    try:
        s.set_customer_action(bol)
    except xmlrpclib.Fault:
        pass


def isHostAddr(value):
    pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    match = pattern.match(value)
    if match:
        return True #match.group()
    else:
        return False


def print_help():
    print 'example: python client.py 192.168.3.130:8000 true'

if __name__ == "__main__":
    args = sys.argv

    if len(args) > 2:
        bol = False
        if 'true' in args[2].lower():
            bol = True
        elif  'false' in args[2].lower():
            bol = False

        if isHostAddr(args[1]):
            switch(args[1],bol)
        else:
            print_help()
    else:
        print_help()
