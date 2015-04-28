__author__ = 'ggh'

from framework.core import jar


class Application(jar.JAR):
    def __init__(self, config):
        super(Application, self).__init__(config)