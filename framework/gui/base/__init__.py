__author__ = 'Administrator'

import data, net

meta = data.Data()


class JIRA():
    def __init__(self):
        self.host = 'http://192.168.3.11:8080'
        self.cookie = None
        self.isActive = False
        self.userName = ''
        self.pagesize = 30


jira = JIRA()


