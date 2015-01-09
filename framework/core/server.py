__author__ = 'guguohai@outlook.com'

import os
import ConfigParser
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

my_data = {'task':'test page','thread_num':1000,'test_num':100,'start':False,'gather_result':False}


class TestServer():
    def __init__(self,data):
        self.data = data

    def get_value(self,key):
        try:
            return self.data[key]
        except KeyError:
            pass

    def set_value(self,key,val):
        self.data[key] = val

    def get_all(self):
        return self.data

def readConfig(selections,opt):
    path_str = PATH('./config.ini')
    conf = ConfigParser.ConfigParser()
    conf.read(path_str)
    return conf.get(selections,opt)

def register():
    import sockets
    host_name = sockets.getfqdn(sockets.gethostname())
    host_addr = sockets.gethostbyname(host_name)
    port = readConfig('server','port')

    server = SimpleXMLRPCServer((host_addr, int(port)))
    server.register_instance(TestServer(my_data))
    server.serve_forever()


if __name__ == "__main__":
    register()


# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ('/RPC2',)
#
# # Create server
# server = SimpleXMLRPCServer(("192.168.3.130", 8000),
#                             requestHandler=RequestHandler)
# # server.register_introspection_functions()
# # server.register_function(set_status,'set')
# # server.register_multicall_functions()
#
# # Run the server's main loop
# server.serve_forever()