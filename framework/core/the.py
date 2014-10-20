__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.util import fs


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


settings = fs.parserConfig(PATH('../../config.ini'))

project_settings = fs.parserConfig(PATH('../../resource/app.ini'))

android = None
web = None
ios = None

i_driver = {'status':False}

androids = fs.parser_to_dict(PATH('../../resource/app.ini'))