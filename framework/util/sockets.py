# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import socket
import time
import constant


def socket_server(host, port, myThread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buff = connection.recv(1024)
            if constant.MSG_START in buff:
                myThread.start_exec()
                connection.send('monitor start...')
            elif constant.MSG_STOP in buff:
                myThread.pause_exec()
                connection.send('monitor stop...')
        except socket.timeout:
            print 'time out'
        connection.close()


def socket_client(host, port, cmd):
    # 客户端连接到监控服务器
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 7556))

    time.sleep(2)
    sock.send(cmd)
    recv_remote = sock.recv(1024)
    sock.close()
    print recv_remote