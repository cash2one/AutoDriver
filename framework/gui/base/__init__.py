__author__ = 'Administrator'

import os
import data, net
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
conf = fs.readConfigs(PATH('../../../config.ini'), 'gui')
meta = data.Data()


class JIRA():
    def __init__(self):
        self.host = conf.get('jira')
        self.cookie = None
        self.isActive = False
        self.default_project = conf.get('default_project')
        self.displayName = ''
        self.userName = ''
        self.pageSize = int(conf.get('page_size'))
        self.follow = []


class Woodpecker():
    def __init__(self):
        self.host = conf.get('woodpecker')


wp = Woodpecker()
jira = JIRA()


