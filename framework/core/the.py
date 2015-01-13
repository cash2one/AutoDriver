__author__ = 'guguohai@pathbook.com.cn'

import os
import uuid
from framework.util import fs

__tpc = ['60eb69a7532a']

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# if uuid.UUID(int=uuid.getnode()).hex[-12:] in __tpc:
# os.path.join(os.path.dirname(__file__), 'templates'),
db_path = ''
settings = fs.parserConfig(PATH('../../config.ini'))
# app_configs = fs.parserConfig(PATH('../../resource/app.ini'))
devices = fs.parser_to_dict(PATH('../../resource/app.ini'))
# products = fs.init_project(PATH('../../resource/app.ini'))

class JIRA():
    def __init__(self):
        _gui = settings['gui']
        self.host = _gui['jira']
        self.cookie = None
        self.isActive = False
        self.default_project = _gui['default_project']
        self.displayName = ''
        self.userName = ''
        self.pageSize = int(_gui['page_size'])
        self.folder = _gui['folder']
        self.follow = []
        self.home = []


class Woodpecker():
    def __init__(self):
        self.host = settings['gui']['woodpecker']

wp = Woodpecker()
jira = JIRA()

taskConfig = fs.task_container(PATH('../../config.ini'), 'task')

