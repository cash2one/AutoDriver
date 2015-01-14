# coding=utf-8
__author__ = 'guguohai@outlook.com'

from framework.core import web


def Application(config):
    platform = config['settings']['platform_name']
    if 'Firefox' in platform:
        return Firefox(config)
    elif 'Chrome' in platform:
        return Chrome(config)


class MyDriver(object):
    '''
    firefox chrome 都通用此类
    '''

    def __init__(self):
        pass

    def method1(self):
        return 'a'


class Firefox(web.Firefox, MyDriver):
    def __init__(self, config):
        super(Firefox, self).__init__(config)


class Chrome(web.Chrome, MyDriver):
    def __init__(self, config):
        super(Chrome, self).__init__(config)


