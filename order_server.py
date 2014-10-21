# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from SimpleXMLRPCServer import SimpleXMLRPCServer

def get_host():
    '''
    获取本机ip地址
    '''
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    host_addr = socket.gethostbyname(host_name)
    return host_addr

def register():
    from framework.core import idriver
    oss = idriver.OrderServer()
    port = idriver.xmlrpc_port()
    host = get_host()

    server = SimpleXMLRPCServer((host, int(port)))
    server.register_instance(oss)
    server.serve_forever()
    print host


if __name__ == "__main__":
    register()