# coding=utf-8
__author__ = 'guguohai@outlook.com'

import io, shutil
import urllib
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class TestHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        buf = 'It works'
        self.protocal_version = 'HTTP/1.1'

        self.send_response(200)

        self.send_header("Welcome", "Contect")
        self.end_headers()
        self.wfile.write(buf)
        #self.process(2)


    def do_POST(self):
        self.process(1)

    def process(self, type):

        content = ""
        if type == 1:  # post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            datas = urllib.unquote(datas).decode("utf-8", 'ignore')  # 指定编码方式
            datas = transDicts(datas)  # 将参数转换为字典
            if datas.has_key('data'):
                content = "data:" + datas['data'] + "\r\n"

        if '?' in self.path:
            query = urllib.splitquery(self.path)
            action = query[0]

            if query[1]:  # 接收get参数
                queryParams = {}
                for qp in query[1].split('&'):
                    kv = qp.split('=')
                    queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
                    content += kv[0] + ':' + queryParams[kv[0]] + "\r\n"

            # 指定返回编码
            enc = "UTF-8"
            content = content.encode(enc)
            f = io.BytesIO()
            f.write(content)
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)

def transDicts(params):
    dicts = {}
    if len(params) == 0:
        return
    params = params.split('&')
    for param in params:
        dicts[param.split('=')[0]] = param.split('=')[1]
    return dicts

def start_server(port):
    http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
    http_server.serve_forever()  # 设置一直监听并接收请求,其中，IP为给localhost设定的访问地址

if __name__ == "__main__":
    start_server(8000)