# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from SimpleXMLRPCServer import SimpleXMLRPCServer


def register():
    '''
    通常order_robot 和 order_server 在一台机器上运行。
    参数都读取自根目录的config.ini [xmlrpc]
    :return:
    '''
    from framework.core import device
    oss = device.OrderServer()
    port = device.xmlrpc_port()
    host = device.xmlrpc_host()#get_host()

    server = SimpleXMLRPCServer((host, int(port)))
    server.register_instance(oss)
    server.serve_forever()
    print host


if __name__ == "__main__":
    #register()
    from framework.core import idriver_android
    idriver_android.customer_server('test.py')

