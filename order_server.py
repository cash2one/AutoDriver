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
    import os
    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )

    def server():
        import socket,subprocess
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(('localhost',7556))
        sock.listen(5)
        while True:
            connection,address = sock.accept()
            #print "client ip is "
            #print address
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                if buf == '1':
                    connection.send('welcome to python server!')
                    #执行一个下订单的脚本
                    #subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
                    py_file=PATH('framework/src/autobook/android/customer/test.py')
                    p = subprocess.Popen("python %s" % py_file, stdout=subprocess.PIPE, shell=True)
                    print p.stdout.read()
            except socket.timeout:
                print 'time out'
            connection.close()
    server()