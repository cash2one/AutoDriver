# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
from framework.core import the
from framework.util import const

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def task_config(test_case_file, inst_class):
    # 获取项目路径，转换成app.init 的sections
    init_size = len(PATH('../../testcase')) + 1
    tar_path = os.path.dirname(test_case_file)
    section = tar_path[init_size:len(tar_path)].replace(os.sep, '.')

    sect = section.lower()
    cfg = the.taskConfig[sect]
    # return sect,cfg
    if cfg[const.PRODUCT] == None:
        the.taskConfig[sect][const.PRODUCT] = inst_class(cfg[const.TASK_CONFIG])
        the.taskConfig[sect][const.PRODUCT].splash()
    return the.taskConfig[sect][const.PRODUCT]


def ios_idr(test_case_file):
    from framework.core.idriver_ios import IOS

    return task_config(test_case_file, IOS)


def android_idr(test_case_file):
    from framework.core.idriver_android import Android

    return task_config(test_case_file, Android)


def firefox_idr(test_case_file):
    from framework.core.idriver_web import Firefox

    return task_config(test_case_file, Firefox)


def firefox_ema(test_case_file):
    from framework.core.emanual_web import Firefox

    return task_config(test_case_file, Firefox)