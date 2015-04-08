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
        # from com.testing.pkg import Calculator


    def find_class(self, clazz):
        mod = __import__(clazz)
        components = clazz.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)

        return mod()


    def splash(self):
        pass

        # ['/Users/ggh/Documents/github/AutoDriver/testcase/MydemoJar', '/Library/Python/2.7/site-packages/pip-1.5.6-py2.7.egg',
        # '/Library/Python/2.7/site-packages/Django-1.7.5-py2.7.egg', '/Library/Python/2.7/site-packages/distribute-0.6.28-py2.7.egg',
        # '/Library/Python/2.7/site-packages/MySQL_python-1.2.4b4-py2.7-macosx-10.9-intel.egg', '/Users/ggh/Documents/github/AutoDriver',
        # '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
        # '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
        # '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
        #  '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC',
        #  '/Library/Python/2.7/site-packages', '/Library/Python/2.7/site-packages/PIL',
        #  u'/Users/ggh/Documents/github/AutoDriver/resource/jar/mytest.jar']




        # class UniqueRandomTest(unittest.TestCase):
        #     def setUp(self):
        #         sys.path.append(PATH('./jar/mytest.jar'))
        #         from com.testing.pkg import Calculator
        #
        #         self.ca = Calculator()
        #
        #
        #     def tearDown(self):
        #         pass
        #
        #     def test_StringValue(self):
        #         result = self.ca.getBoolResult(6, 3)
        #         self.assertEquals(result, True)