# coding=utf-8
__author__ = 'guguohai@outlook.com'

import os
from PyQt4.QtGui import *
from PyQt4 import QtCore
from framework.util import constant
from framework.gui.views import monitor_ui
from framework.gui.helpers import monitor_ext


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MonitorDialog(QDialog, monitor_ui.Ui_Dialog):
    def __init__(self):
        super(MonitorDialog, self).__init__()

        self.setupUi(self)
        self.setFont(QFont("Microsoft YaHei", 9))
        self.btn_end.hide()

        self.btn_start.clicked.connect(self.start_monitor)
        self.btn_end.clicked.connect(self.end_monitor)
        self.chk_server.clicked.connect(self.check_server)
        # self.chk_server.stateChanged.connect(self.check_server)
        self.isChecked = False
        self.reqThread = None
        self.mtThread = None
        self.host = ''
        self.port = 80
        self.sock = None

    def start_monitor(self):
        self.btn_start.hide()
        self.btn_end.show()

        host_str = self.txt_host.text()
        if monitor_ext.isHostAddr(host_str):
            self.host = host_str
            self.port = int(self.txt_port)
            self.sock = monitor_ext.Socketer(self.host, self.port)
            if self.chk_server.isChecked():
                if self.task_thread == None:
                    self.task_thread = monitor_ext.TaskThread(self.host, constant.TASK_SERVER)
                    self.task_thread.start()
                self.sock.server(self.mtThread)
            else:
                self.sock.client(constant.MSG_START)
        else:
            QMessageBox.warning(self, u'地址错误',
                                u"\n服务器地址格式错误，请重新填写？",
                                QMessageBox.Abort)

    def end_monitor(self):
        ret = QMessageBox.warning(self, u'停止监控',
                                  u"\n是否停止监控并收集测试结果？",
                                  QMessageBox.Yes | QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.sock.client(constant.MSG_STOP)
            # self.file_dialog()接收到数据后，打开保存对话框
        elif ret == QMessageBox.Cancel:
            pass

    def check_server(self):
        if not self.isChecked:
            ret = QMessageBox.warning(self, u'确认选择',
                                      u"\n是否把本机设置为被监控对象？",
                                      QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                self.chk_server.setChecked(True)
                self.isChecked = True
                self.txt_host.setText(monitor_ext.get_ip_address())
            elif ret == QMessageBox.Cancel:
                self.chk_server.setChecked(False)
                self.isChecked = False
        else:
            self.chk_server.setChecked(False)
            self.isChecked = False

    def file_dialog(self):
        fd = QFileDialog(self)
        self.filename = fd.getSaveFileName()
        fobj = open(self.filename, 'w')
        fobj.write(self.txt_msg.toPlainText())
        fobj.close()
        self.txt_msg.setText('File saved!!')
        # fd.getOpenFileName()
        # from os.path import isfile
        #
        # if isfile(self.filename):
        # s = open(self.filename, 'r').read()
        #
        # def handler(self, msg):
        # sock = monitor_ext.Socketer(self.host, self.port)
        #     if msg == '-server':
        #         if self.mtThread == None:
        #             self.mtThread = monitor_ext.TaskThread(self.host, constant.TASK_SERVER)
        #             self.mtThread.start()
        #         sock.server(self.mtThread)
        #     elif msg == '-req':
        #         if self.reqThread == None:
        #             self.reqThread = monitor_ext.TaskThread(self.host, constant.TASK_LOCAL)
        #             self.reqThread.start()
        #         sock.server(self.reqThread)
        #     elif msg == '-start':
        #         sock.client(constant.MSG_START)
        #         sock.client(constant.MSG_START)
        #     elif msg == '-stop':
        #         sock.client(constant.MSG_STOP)
        #         sock.client(constant.MSG_STOP)

