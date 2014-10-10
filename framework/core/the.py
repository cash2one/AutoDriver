__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.util import fs


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

settings = fs.parserConfig(PATH('../../config.ini'))

android = None
web = None
ios = None

i_driver = {'status':False}