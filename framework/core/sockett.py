# coding=utf-8
__author__ = 'Administrator'

import socket,sys

def server():
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
            #else:
                #connection.send('please go out!')
        except socket.timeout:
            print 'time out'
        connection.close()

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',7556))
    import time
    time.sleep(2)
    sock.send('1')
    print sock.recv(1024)
    sock.close()




if __name__ == "__main__":

    args = sys.argv
    if args[1]=='-server':
        server()
    elif args[1]=='-client':
        client()