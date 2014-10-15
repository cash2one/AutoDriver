# coding=utf-8
__author__ = 'Administrator'

import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from framework.core import extend,idriver


class MonitorThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.dbm = None
        self.mail_to = readConfig('server','mail')
        self.sev = self.connect_server(get_host(),int(readConfig('server','port')))


    def run(self):
        while not self.thread_stop:

            if self.is_start():
                if self.dbm == None:
                    self.dbm = save_data()
                try:
                    args = sinfo.poll(1)
                    sinfo.refresh_window(self.dbm,*args)
                except (KeyboardInterrupt, SystemExit):
                    pass
            else:
                if self.dbm != None:
                    self.dbm.conn.close()
                    send_mail(self.mail_to)
                    self.dbm = None

                time.sleep(3)
