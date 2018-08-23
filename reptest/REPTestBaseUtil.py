import httplib2
from HttpMethod.ThreadPoolComplex import ThreadPool
import socket

class REPTestBaseUtil(object):

    REP=[]

    def __init__(self,Rep_info):
        self.REP=Rep_info
        socket.setdefaulttimeout(10)

    def TestMethod(self,method_name,args):
        if method_name == "ProxyMessagePush":
            return self.ProxyMessagePush(*args)
        else:
            return "Not Fount Method"

    def ProxyMessagePush(self,url=None,method="GET",param=None,headers={}):
        success_count = 0
        http = httplib2.Http()
        if len(self.REP) > 0:
            for rep_ip_port in self.REP:
                if url is not None:
                    if param is not None:
                        param=""
                    try:
                        resp_headers,content = http.request(uri="http://" + rep_ip_port + url, method=method, body=param, headers=headers)
                    except Exception as e:
                        print(e,rep_ip_port)
                        continue
                    if resp_headers["status"] == "200":
                        print(str(content),'-------------',rep_ip_port)
                        success_count+=1
                    else:
                        print(resp_headers["status"],"http://" + rep_ip_port + url)
        else:
            return "REP Size is 0"

        return "success_count:" + str(success_count)