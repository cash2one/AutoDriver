__author__ = 'Administrator'

import os
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

guis = fs.readConfigs(PATH('../../../config.ini'), 'gui')

class JIRA():
    def __init__(self):
        self.host = guis.get('jira')
        self.cookie = None
        self.isActive = False
        self.default_project = guis.get('default_project')
        self.displayName = ''
        self.userName = ''
        self.pageSize = int(guis.get('page_size'))
        self.folder = guis.get('folder')
        self.follow = []


class Woodpecker():
    def __init__(self):
        self.host = guis.get('woodpecker')


wp = Woodpecker()
jira = JIRA()


