# coding=utf-8
__author__ = 'Administrator'

import socket
import httplib2
import json

class WebInterface():

    def __init__(self,addr):
        self.addr = addr
        socket.setdefaulttimeout(5.0)

    def assertResult(self,key_str):
        h = httplib2.Http(".cache")
        (resp, content) = h.request(self.addr, "GET",
                            headers={'cache-control':'no-cache'})
        if resp.status==200:
            s=json.loads(content)

            #return s.keys()#s['weatherinfo']['city']
            #return s.keys()[0]
            for key in s.keys():
                return s[key][0]
                #pass



            #return s["weatherinfo"].encode('ascii')
        else:
            return resp.status




