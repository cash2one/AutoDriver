# coding=utf-8
__author__ = 'guguohai@outlook.com'

import time
from framework.core import web


def Application(config):
    platform = config['settings']['platform_name']
    if 'Firefox' in platform:
        return Firefox(config)
    elif 'Chrome' in platform:
        return Chrome(config)


class MyDriver(object):
    '''
    firefox chrome 继承此类
    '''

    def __init__(self):
        pass

    def example(self):
        return 'test'


class Firefox(web.Firefox, MyDriver):
    def __init__(self, config):
        super(Firefox, self).__init__(config)

    def splash(self):
        ini_url = self.settings['url']
        self.get(ini_url)


        self._index_url(ini_url)
        time.sleep(2)


class Chrome(web.Chrome, MyDriver):
    def __init__(self, config):
        super(Chrome, self).__init__(config)
