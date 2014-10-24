__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.util import fs


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

app_ini = PATH('../../resource/app.ini')

settings = fs.parserConfig(PATH('../../config.ini'))

project_settings = fs.parserConfig(app_ini)

devices = fs.parser_to_dict(app_ini)
