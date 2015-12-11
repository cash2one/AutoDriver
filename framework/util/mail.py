# coding=utf-8
__author__ = 'gghsean@163.com'

import os
import smtplib
import mimetypes
import email
import zipfile

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Mail():

    def __init__(self,file_path):
        self.file_path = file_path
        self.zipAttach()

    def mail_content(self,m_from, m_to, m_title, m_txt):
        e_mail = email.MIMEMultipart.MIMEMultipart()
        text_msg = email.MIMEText.MIMEText(m_txt, _charset="utf-8")
        e_mail.attach(text_msg)

        #att_name = os.path.join(self.file_path,'result.zip')#PATH('../../result/result.zip')

        #读入文件内容并格式化
        data = open(self.file_path, 'rb')
        ctype, encoding = mimetypes.guess_type(self.file_path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'

        maintype, subtype = ctype.split('/', 1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        #附件编码
        email.Encoders.encode_base64(file_msg)

        #邮件头
        file_msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.file_path))
        e_mail.attach(file_msg)

        e_mail['From'] = m_from
        e_mail['To'] = m_to
        e_mail['Subject'] = m_title
        e_mail['Date'] = email.Utils.formatdate()

        #格式化
        return e_mail.as_string()

    def zipAttach(self):
        zip_file = os.path.join(self.file_path,'result.zip')

        zip = zipfile.ZipFile(zip_file, 'w' ,zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(self.file_path, True):
            for filaname in filenames:
                direactory = os.path.join(dirpath,filaname)
                zip.write(direactory)

        zip.close()

    def send_mail(self,From, To, mail_title, mail_txt):
        mail_server = smtplib.SMTP("smtp.163.com")
        mail_server.login("pathbook@163.com", "tupugongsi") #smtp服务器需要验证时
        mail_con = self.mail_content(From, To, mail_title, mail_txt)
        try:
            mail_server.sendmail(From, To, mail_con)
        finally:
            mail_server.quit()
