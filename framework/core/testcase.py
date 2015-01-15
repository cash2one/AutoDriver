# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import sys
import os
from framework.core import the
from framework.util import const, fs

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def app(test_case_file):
    '''
    初始化用例，装载容器
    :param test_case_file:
    :return:
    '''
    # 获取项目路径，转换成app.init 的sections
    init_size = len(PATH('../../testcase')) + 1
    tar_path = os.path.dirname(test_case_file)
    section = tar_path[init_size:len(tar_path)].replace(os.sep, '_')

    sect = section.lower()
    cfg = the.taskConfig[sect]

    if cfg[const.PRODUCT] == None:
        # configs = fs.parserConfig(PATH('../../resource/app/%s' % cfg[const.TASK_CONFIG]))
        manifest = fs.parserConfig(PATH('../../manifest/%s' % cfg[const.TASK_CONFIG]))

        m = my_import('drivers.%s' % section)
        the.taskConfig[sect][const.PRODUCT] = m.Application(manifest)

        the.taskConfig[sect][const.PRODUCT].splash()
    return the.taskConfig[sect][const.PRODUCT]
