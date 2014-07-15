# coding=utf-8
__author__ = 'guohai'

import json
from util import http


#从接口从获取json
def find_jsons(action_url):
    resp,content=http.getHttp(action_url)
    if resp.status==200:
        return json.loads(content)#.decode('utf8')
        #return json.dumps(ss, ensure_ascii=False)
    else:
        return None

#字符串转换json格式
def fromStr(content):
    return json.loads(content)


# def find_value_by_key(json,key):
#     return findKeys(json,key)

#递归查找key的value
def find_value_by_key(json,key):
    if isinstance(json,dict):
        for json_result in json.values():
            if key in json.keys():
                return json.get(key)
            else:
                find_value_by_key(json_result,key)
    elif isinstance(json,list):
        for json_array in json:
            find_value_by_key(json_array,key)


    # def assertResult(self,key_str):
    #     h = httplib2.Http(".cache")
    #     (resp, content) = h.request(self.addr, "GET",
    #                         headers={'cache-control':'no-cache'})
    #     if resp.status==200:
    #         s=json.loads(content)
    #
    #         #return s.keys()#s['weatherinfo']['city']
    #         #return s.keys()[0]
    #         for key in s.keys():
    #             return s[key][0]
    #             #pass
    #
    #         #return s["weatherinfo"].encode('ascii')
    #     else:
    #         return resp.status

    # _MAX_LENGTH = 80
    # longMessage = False
    # failureException = AssertionError
    # def assertTrue(self, expr, msg=None):
    #     """Check that the expression is true."""
    #     if not expr:
    #         msg = self._formatMessage(msg, "%s is not true" % self.safe_repr(expr))
    #         raise self.failureException(msg)
    #
    #
    # def safe_repr(self,obj, short=False):
    #     try:
    #         result = repr(obj)
    #     except Exception:
    #         result = object.__repr__(obj)
    #     if not short or len(result) < self._MAX_LENGTH:
    #         return result
    #     return result[:self._MAX_LENGTH] + ' [truncated]...'
    #
    # def _formatMessage(self, msg, standardMsg):
    #     if not self.longMessage:
    #         return msg or standardMsg
    #     if msg is None:
    #         return standardMsg
    #     try:
    #         return '%s : %s' % (standardMsg, msg)
    #     except UnicodeDecodeError:
    #         return  '%s : %s' % (self.safe_repr(standardMsg), self.safe_repr(msg))
    #
