# coding=utf-8
__author__ = 'Administrator'

import os
import sys
import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from framework.gui.ui import jira_main_ui
from framework.core import the

JIRA_URL = 'http://192.168.3.11:8080'
#http://192.168.3.11:8080/rest/api/2/project
#http://192.168.3.11:8080/rest/api/2/search?jql=project+%3D+{0}&startAt={1}&maxResults={2}

class MainForm(QWidget, jira_main_ui.Ui_Form):
    def __init__(self, parent_widget):
        super(MainForm, self).__init__()

        self.setupUi(parent_widget)

    def getData(self, project_name, start=0, end=10):
        # project = 'IDRIVERC'
        # start = '10'
        # end = '20'
        if the.JIRA != None:
            p = the.JIRA.get(
                '/rest/api/2/search?jql=project+%3D+' + project_name + '&startAt=' + start + '&maxResults=' + end)

            self.lbl_bug.setText(str(p['maxResults']))