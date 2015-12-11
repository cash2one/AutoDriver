# coding=utf-8
__author__ = 'gghsean@163.com'

import sys
import os
import time

#from PyQt4 import QtGui

from framework.core import task, data, box
from framework.util import mail
#from woodpecker import main as ui


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

root_dir = os.path.dirname(__file__)


def createDatabase():
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    box.db_path = 'report' + time_str + '.db'

    gdata = data.generateData(os.path.join(root_dir, box.db_path),PATH('./resource/xls/'))
    gdata.close()


def start():
    case_list = [
        {'cases': {'test_customer_allfinishOrder': 5, 'test_customer_callServer_xgh': 3}, 'status': 0,
         'path': 'testcase/AutobookClient/customer'},
        {'cases': {'test_driver_cmEarnings_zc': 3, 'test_driver_completeOrder_info__zc': 2}, 'status': 0,
         'path': 'testcase/AutobookClient/driver'}
    ]

    task_list = []
    for c in case_list:
        t = task.Task(c)
        task_list.append(t)

    runner = task.TestRunner(task_list)
    runner.start()


def startReport():
    '''
    测试完成，生成静态html报告
    :return:
    '''
    import webbrowser
    from framework.core import report

    rp = report.Report(data.getDatabasePath(root_dir), 25)
    rp.start()
    webbrowser.open(PATH('./report/index.html'))


def sendMail(mail_to):
    '''
    把静态html打包后，发送邮件
    :param mail_to:
    :return:
    '''
    path = PATH('./report/')
    if os.path.isdir(path):
        if os.path.exists(os.path.join(path, 'report.zip')):
            # mail_list = ['19319752@qq.com','gghsean@163.com']
            # mail_to = ','.join(mail_list)
            m = mail.Mail(PATH('./report/'))
            mail_title = 'testss'
            mail_content = '一封邮件的内容'
            m.send_mail('gghsean@163.com', mail_to, mail_title, mail_content)
        else:
            pass  # 生成文件 及压缩包

    else:
        pass  # 文件夹，生成文件 及压缩包


# def gui():
#     app = QtGui.QApplication(sys.argv)
#     mainWin = ui.MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())


def help():
    print u'''
        自动化脚本帮助列表：\n
        -start     执行脚本\n
        -robot     启动订单机器人\n
        -report    生成测试报告\n
        -mail      打包测试报告并以邮件发送
        '''


def main():
    args = sys.argv

    if len(args) > 1:
        if args[1] == "-start":
            start()
        elif args[1] == "-report":
            startReport()
        #elif args[1] == "-woodpecker":
            #gui()
        elif args[1] == "-help":
            help()
        elif args[1] == "-mail":
            if len(args) > 2 and args[2] != '':
                sendMail(args[2])
            else:
                print u'参数错误，[run.py -m 参数]'
        else:
            print u'查看帮助 -h'
    else:
        print u'查看帮助 -h'


if __name__ == "__main__":
    main()


    # dr = device.RunAppium(4725)
    # dr.start()
    # #
    # # p1 = subprocess.Popen('appium --port 4725',stdout=subprocess.PIPE,shell=True)
    # # os.popen('appium --port 4725')
    # #
    # # aa = p1.stdout.read()
    # # if 'debug: Non-default server args: {"port":4725}' in aa:
    #
    #
    # while 1:
    # print 'gegwwwwww'
    # time.sleep(2)

    # p1 = subprocess.Popen('appium --port %s' % 4723, stdout=subprocess.PIPE, shell=True)
    # p1.stdout.read()
    #
    # p2 = subprocess.Popen('appium --port %s' % 4726, stdout=subprocess.PIPE, shell=True)
    # p2.stdout.read()
