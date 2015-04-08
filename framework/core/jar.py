__author__ = 'ggh'

import os
import sys


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JAR(object):
    def __init__(self, config):
        self.config = config
        self.settings = self.config['settings']

        jar_path = PATH('../../resource/jar/' + self.settings['jar'])
        sys.path.append(jar_path)


    def find_class(self, clazz):
        mod = __import__(clazz)
        components = clazz.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)

        return mod()


    def splash(self):
        pass
