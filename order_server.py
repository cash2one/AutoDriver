# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from SimpleXMLRPCServer import SimpleXMLRPCServer

def register():
    from framework.core import idriver
    oss = idriver.OrderServer()
    host_addr = idriver.get_host()
    port = idriver.get_port()

    server = SimpleXMLRPCServer((host_addr, int(port)))
    server.register_instance(oss)
    server.serve_forever()


if __name__ == "__main__":
    register()