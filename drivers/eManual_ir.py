# coding=utf-8
__author__ = 'guguohai@outlook.com'

from framework.core import web


class Application(web.Firefox):
    def __init__(self, config):
        super(Application, self).__init__(config)
