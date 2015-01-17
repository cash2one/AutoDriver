# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.core import the
from framework.util import const, fs
from selenium.common import exceptions
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCase(unittest.TestCase):
    def __init__(self):
        super(TestCase, self).__init__()

        self.exceptions = exceptions

    def app(self, file_):
        '''
        初始化用例，装载容器
        :param test_case_file:
        :return:
        '''
        # 获取项目路径，转换成app.init 的sections
        init_size = len(PATH('../../testcase')) + 1
        tar_path = os.path.dirname(file_)
        section = tar_path[init_size:len(tar_path)].replace(os.sep, '_')

        sect = section.lower()
        cfg = the.taskConfig[sect]

        if cfg[const.PRODUCT] == None:
            # configs = fs.parserConfig(PATH('../../resource/app/%s' % cfg[const.TASK_CONFIG]))
            manifest = fs.parserConfig(PATH('../../manifest/%s' % cfg[const.TASK_CONFIG]))

            class_name = 'drivers.%s' % section
            mod = __import__(class_name)
            components = class_name.split('.')
            for comp in components[1:]:
                mod = getattr(mod, comp)

            the.taskConfig[sect][const.PRODUCT] = mod.Application(manifest)

            the.taskConfig[sect][const.PRODUCT].splash()
        return the.taskConfig[sect][const.PRODUCT]



