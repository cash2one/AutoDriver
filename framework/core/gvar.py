__author__ = 'Administrator'

import os
from framework.core import device


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

driver = device.android(PATH('../../resource/MyChevy_1.2.0.apk'))

mainActivity = None
mainContext = None