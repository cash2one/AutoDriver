# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

import os
import sys
import shutil
import time
import re
import uuid
import os
import webbrowser
from framework.util import sqlite, mail,fs
from framework.core import the,data,device,task,report, routine, HTMLTestRunner

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

report_dir = './report'
case_dir='./testcase/'
src_dir='./framework/src/'
xls_path = './resource/xls/'
root_dir = os.path.dirname(__file__)


def createDatabase():
    time_str= time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    the.db_path = 'report'+time_str + '.db'

    gdata = data.generateData(PATH('./resource/xls/'),os.path.join(root_dir,the.db_path))
    gdata.close()


#初始化
def init():
    print u'初始化中，请稍候...'

    xlss = data.getExcelsData(PATH(xls_path),False)

    #生成testcase文件夹
    if not os.path.isdir(PATH(case_dir)):
        os.makedirs(PATH(case_dir))
        f=open(PATH(case_dir+'__init__.py'),'w+')
        f.close()
    time.sleep(2)

    fs.prepareFile(xlss,PATH(src_dir),PATH(case_dir))

    time.sleep(2)
    createDatabase()
    print u'初始化完成，输入[run.py -s]运行'



def start():
    d = device.android(the.settings['android_mychevy'])
    xlss = data.getExcelsData(PATH(xls_path),False)
    tk = task.Task(False,xlss)
    # #TODO: 需要加入android启动的等待时间
    #
    serv = routine.TaskAction(tk,data.getDatabasePath(root_dir))
    serv.start()
    print u'脚本已经开始执行.....'

    #oldRunner(tk.getTestSuite())


def startStress():
    stress_settings = the.settings['stress']
    stress.start(stress_settings)


def startReport():
    '''
    测试完成，生成静态html报告
    :return:
    '''
    rp = report.Report(data.getDatabasePath(root_dir),25)
    rp.start()
    webbrowser.open(PATH('./report/index.html'))


def oldRunner(suite):
    '''
    第三方测试报告生成
    :param suite:
    :return:
    '''
    reportDir=sys.path[0] + os.sep +'abc.html'
    fp = open(reportDir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况'
    )
    runner.run(suite)

def sendMail(mail_to):
    '''
    把静态html打包后，发送邮件
    :param mail_to:
    :return:
    '''
    path =PATH('./report/')
    if os.path.isdir(path):
        if os.path.exists(os.path.join(path,'report.zip')):
            #mail_list = ['19319752@qq.com','gghsean@163.com']
            #mail_to = ','.join(mail_list)
            m = mail.Mail(PATH('./report/'))
            mail_title = 'testss'
            mail_content = '一封邮件的内容'
            m.send_mail('gghsean@163.com',mail_to,mail_title,mail_content)
        else:
            pass#生成文件 及压缩包

    else:
        pass#文件夹，生成文件 及压缩包


def help():
    print u'''
        自动化脚本帮助列表：\n
        -i      初始化脚本\n
        -s      执行脚本\n
        -stress 性能测试\n
        -r      生成测试报告\n
        -m      打包测试报告并以邮件发送
        '''

#order = {'-i':init(),'-s':start(),'-r':startReport(),'-m':sendMail(''),'-h':help()}

def main():
    args = sys.argv

    # order[args[1]]
    if len(args) > 1:
        if args[1]=='-i':
            init()
        elif args[1]=="-s":
            start()
        elif args[1]=="-stress":
            startStress()
        elif args[1]=="-r":
            startReport()
        elif args[1]=="-h":
            help()
        elif args[1]=="-m":
            if len(args)>2 and args[2]!='':
                sendMail(args[2])
            else:
                print u'参数错误，[run.py -m 参数]'
        else:
            print u'查看帮助 -h'
    else:
        print u'查看帮助 -h'


if __name__ == "__main__":
    main()


    #init()
    # a,b=data.sortTestCase(PATH('./resource/xls/autobook_interface_app.xls'))
    #
    # for aa in b:
    #     print aa


    # for i in range(1,len(products)):
    #     if products[i] in db_data.os:


    #start()
    # from collections import defaultdict
    # desc_list = []
    # for x in xlss:
    #     for d in x['desc'].split('|'):
    #         desc_list.append(x['desc'].split('?')[0])
    #
    # d = defaultdict(list)
    # for k,va in [(v,i) for i,v in enumerate(desc_list)]:
    #     d[k].append(va)
    # print  d.items()

    # import json
    # aa= '{"res":"0","test":["test1","test2"],"myv":[{"t":"t1","tt":"t2"},{"q":"q1","qq":"q2"}],"tokenNo":"fgw","msg":{"tokenNo":"fgw","orders":[{"orderno":"135","hasEval":"1"}],"ord":"oo"}}'
    # bb='{"msg": {"list": []}, "res": "0"}'
    # cc = '{"res":"0","msg":{"list":[1]}}'
    # j = json.loads(cc)
    # #json_v = json.loads()
    # rules={'tokenNo':'','test':''}
    # print interface.walkJson(j,rules)
    #

    #
    # from PIL import Image
    # import subprocess
    # file_name = 'screenshot123333.png'
    # cmd = 'adb shell /system/bin/screencap -p /sdcard/' + file_name
    # cmd_pull = 'adb pull /sdcard/screenshot.png d:/' + file_name
    # p1 = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # # p.communicate()  # Returns (stdoutdata, stderrdata): stdout and stderr are ignored, here
    # # if prog.returncode:
    # #     raise Exception('program returned error code {0}'.format(prog.returncode))
    #
    # curline = p1.stdout.readline()
    # while(curline != ""):
    #     #print (curline)
    #     curline = p1.stdout.readline()
    #     p1.wait()


    # timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    # os.popen("adb wait-for-device")
    # os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    # if not os.path.isdir(PATH('./screenshot/')):
    #     os.makedirs(PATH('./screenshot/'))
    #     os.popen("adb pull /data/local/tmp/tmp.png " + PATH("./screenshot/" + timestamp + ".png"))
    #     os.popen("adb shell rm /data/local/tmp/tmp.png")
    #     print "success"

    # from framework.core import image
    # print image.isSame(PATH('./screenshot/a.png'),PATH('./screenshot/b.png'))














