# 检查代理可用性
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from HttpMethod import ThreadPoolComplex


allSize = 0
useSize = 0
pool = object()
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# 请求方法
def proxy_request(url, method="GET", param=None, headers=None, proxies=None, timeout=10):
    if url is not "":
        result = requests.request(method=method, url=url, headers=headers, proxies=proxies, timeout=timeout)
    else:
        result = "无连接"
    return result

# 使用代理访问12306
def proxyTest(proxies):
    try:
        result = proxy_request(
            # url="https://kyfw.12306.cn/otn/leftTicket/init",
            url="https://www.baidu.com/",
            timeout=10,
            proxies=proxies,
            headers=headers)
        if result == "无连接" or result.status_code != 200 or len(str(result.content)) <= 0:
            return False
        else:
            return True
    except Exception:
        return False

# 验证
def check(ip):
    proxies = {
        "https": "http://" + ip + ":3138"
    }
    flag = proxyTest(proxies)
    if flag != True:
        print(ip, flag)
    return flag

def checkResult(status, result):
    global allSize
    global useSize
    allSize -= 1
    if result:
        useSize += 1
    if allSize == 0:
        global pool
        print('可用:', useSize)
        pool.terminate()

# 获取代理IP
def getCallNewIp(pool):
    global allSize
    urls = {
        # 'http://cloudmonitorproxy.51kongtie.com/Proxy/getProxyByServiceType?proxyNum=500&serviceType=3'
        # ,
        'http://cloudmonitorproxy.51kongtie.com/Proxy/getProxyByServiceType?proxyNum=500&serviceType=4'
    }
    proxys = []
    for proxyUrl in urls:
        proxyStr = requests.request(method='GET', url=proxyUrl, headers=headers, timeout=10)
        proxys = proxys + proxyStr.json()
    allSize = len(proxys)
    print('所有:', allSize)
    for proxy in proxys:
        pool.run(func=check, args=(proxy['proxyIP'],), callback=checkResult)

# 验证代理是否可用
def execute(pool):
    getCallNewIp(pool)
    pass

# 启动任务
def startJob(scheduler, second):
    # 线程池
    global pool
    pool = ThreadPoolComplex.ThreadPool(50)
    execute(pool)
    # 添加任务
    # scheduler.add_job(execute,"interval",seconds=second)
    # 启动Job
    # scheduler.start()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    startJob(scheduler=scheduler, second=60000)
