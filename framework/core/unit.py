# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import sys
from framework.core import the
from framework.util import const, fs
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestCase, self).__init__(methodName)

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

    def func_name(self):
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        return f.f_code.co_name  # (f.f_code.co_name, f.f_lineno)


    def assertTrue(self, expr, msg=None):
        expect_str = u'期望结果还未读取用例...'
        expect_msg = u'【期望结果】\r\n%s\r\n\r\n' % expect_str
        actual_msg = u'【实际结果】\r\n%s' % msg
        super(TestCase, self).assertTrue(expr, expect_msg + actual_msg)


