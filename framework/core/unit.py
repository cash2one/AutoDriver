# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import sys
import re
from framework.core import the
from framework.util import const, fs
import unittest
import inspect

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


class TestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestCase, self).__init__(methodName)
        self.file_text = ''

    def app(self, file_):
        '''
        初始化用例，装载容器
        :param test_case_file:
        :return:
        '''
        # 获取项目路径，转换成app.init 的sections
        # func = inspect.getframeinfo(inspect.currentframe().f_back)
        # print 'func::',os.path.dirname(func[0])
        #self.file_text = self.__pyContent(file_)

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

    # def func_name(self):
    # """Return the frame object for the caller's stack frame."""
    # try:
    # raise Exception
    # except:
    # f = sys.exc_info()[2].tb_frame.f_back
    # return f.f_code.co_name  # (f.f_code.co_name, f.f_lineno)

    # def __pyContent(self, path):
    #     path_ = path.replace('.pyc', '.py')
    #     file_object = open(path_)
    #     file_con = ''
    #     try:
    #         file_con = file_object.read()
    #     finally:
    #         file_object.close()
    #     return file_con
    #
    # def __read_notes(self, func):
    #     sign_str = "'''"
    #     func_index = self.file_text.find(func)
    #     note = self.file_text[func_index:]
    #
    #     notes_s = note.find(sign_str) + len(sign_str)
    #     if notes_s > len(sign_str):
    #         note_c = note[notes_s:]
    #         note_e = note_c.find(sign_str)
    #         return note_c[0:note_e].replace(':return:', '').strip()
    #     else:
    #         return 'null'

    def assertTrue(self, expr, msg=None):
        func = inspect.getframeinfo(inspect.currentframe().f_back)[2]
        # expect_str = self.__read_notes(func[2])
        expect_str = eval('self.__class__.%s.__doc__' % func)

        expect_msg = u'【期望结果】\r\n' + expect_str.replace(':return:', '').strip()
        actual_msg = u'\r\n\r\n【实际结果】\r\n' + msg
        super(TestCase, self).assertTrue(expr, expect_msg + actual_msg)


