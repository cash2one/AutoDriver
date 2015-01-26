# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.core import box
from framework.util import const, fs
import unittest
from unittest import util as unitutil
import inspect

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
        # func = inspect.getframeinfo(inspect.currentframe().f_back)
        # print 'func::',os.path.dirname(func[0])
        # self.file_text = self.__pyContent(file_)

        init_size = len(PATH('../../testcase')) + 1

        tar_path = os.path.dirname(inspect.stack()[1][1])  # file_)
        section = tar_path[init_size:len(tar_path)].replace(os.sep, '_')

        sect = section.lower()
        cfg = box.taskConfig[sect]

        if cfg[const.PRODUCT] == None:
            manifest = fs.parserConfig(PATH('../../manifest/%s' % cfg[const.TASK_CONFIG]))

            class_name = 'drivers.%s' % section
            mod = __import__(class_name)
            components = class_name.split('.')
            for comp in components[1:]:
                mod = getattr(mod, comp)

            box.taskConfig[sect][const.PRODUCT] = mod.Application(manifest)
            box.taskConfig[sect][const.PRODUCT].splash()

        return box.taskConfig[sect][const.PRODUCT]

    def __doc(self, title, origin_txt):
        if not type(origin_txt) is unicode:
            orgin = origin_txt.replace(':return:', '')
            return title + '\r\n' + unicode(orgin.strip(), "utf-8")
        else:
            return origin_txt

    def __msg(self, func_name, msg):
        c_note = eval('self.__class__.__doc__')
        f_note = eval('self.__class__.%s.__doc__' % func_name)
        heads = [u'【说明】', u'【期望结果】'], u'【实际结果】'

        step = '' if c_note == None else self.__doc(heads[0], c_note) + '\r\n\r\n'
        expect = '' if f_note == None else self.__doc(heads[1], f_note) + '\r\n\r\n'
        actual = '' if msg == None else self.__doc(heads[2], msg)

        return step + expect + actual

    def assertTrue(self, expr, msg=None):
        # func = inspect.getframeinfo(inspect.currentframe().f_back)[2]
        # expect_str = self.__read_notes(func[2])
        func_name = inspect.stack()[1][3]
        super(TestCase, self).assertTrue(expr, self.__msg(func_name, msg))

    def assertFalse(self, expr, msg=None):
        func_name = inspect.stack()[1][3]
        super(TestCase, self).assertFalse(expr, self.__msg(func_name, msg))

    def assertEqual(self, first, second, msg=None):
        func_name = inspect.stack()[1][3]
        super(TestCase, self).assertEqual(first, second, self.__msg(func_name, msg))


        # def my_import(name):
        # mod = __import__(name)
        # components = name.split('.')
        # for comp in components[1:]:
        # mod = getattr(mod, comp)
        # return mod