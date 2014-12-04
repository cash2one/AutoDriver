__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.util import fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# os.path.join(os.path.dirname(__file__), 'templates'),

settings = fs.parserConfig(PATH('../../config.ini'))

app_configs = fs.parserConfig(PATH('../../resource/app.ini'))

devices = fs.parser_to_dict(PATH('../../resource/app.ini'))

products = fs.init_project(PATH('../../resource/app.ini'))
