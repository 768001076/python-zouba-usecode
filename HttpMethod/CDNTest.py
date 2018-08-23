import re
import os
import sys
import socket
import requests
class Testurl(object):

    def __init__(self,proxy,url):
        self.proxy   = proxy
        self.url     = url
        self.proxies = {}
        self.repeat  =  []

    def FilterNode(self):
        while True:
            nodeip   = socket.gethostbyname(self.proxy)
            self.repeat.append(nodeip)
            if self.repeat.count(nodeip) <= 1000:
                pass
            else:
                break

    def StartTest(self):
        for x in self.repeat:
            try:
                self.proxies['http://'] = ['http://%s:80' % str(x)]
                result = requests.get(self.url,proxies = self.proxies)
                status = re.search('[+[0-9]+]',str(result))
            except Exception as e:
                print('\033[40;31m错误\033[0m:请手动尝试检测\n1:不指定节点是否通\n2:测试URL是否为Http')
                sys.exit(1)
            if   status.group() == '[200]':
                print('\033[40;32m%s 200 OK\033[0m' % (x))
            elif status.group() == '[404]':
                print('\033[40;31m%s 404 Not Found\033[0m' % (x))
            elif status.group() == '[403]':
                print('\033[40;31m%s 403 Forbidden\033[0m' % (x))
            elif status.group() == '[301]':
                print('\033[40;33m%s 301 Moved Permanently\033[0m'% (x))
            elif status.group() == '[302]':
                print('\033[40;33m%s 302 Fount\033[0m'% (x))
            else:
                print('\033[40m34m无法识别\033[0m' % (x))
        print(result.text)
def Help():
        print('\033[40;33m-d 指定厂商CNAME\n-h 指定测试URL\033[0m')
if __name__ == '__main__':
    try:
            proxy="115.204.29.233"
            value = Testurl(proxy,"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-04-13&leftTicketDTO.from_station=BXP&leftTicketDTO.to_station=SJP&purpose_codes=ADULT")
            value.FilterNode()
            value.StartTest()
    except(IndexError,SyntaxError):
            Help()