#刷新出访IP
from sqlserverdatabaseutil import VPSServerUtil
from apscheduler.schedulers.blocking import BlockingScheduler
from linuxmethod import BasicSSHUtil as bsSsh
import requests
from HttpMethod import ThreadPoolComplex

def proxy_request(url, method="GET", param=None, headers=None, proxies=None, timeout=10):
    if url is not "":
        result = requests.request(method=method, url=url, headers=headers, proxies=proxies, timeout=timeout)
    else:
        result = "无连接"
    return result

def proxyTest(SshLoginIp, SshLoginPort,proxies):
    try:
        result = proxy_request(
            url="https://kyfw.12306.cn/otn/leftTicket/init",
            timeout=10,
            proxies=proxies)
        if result=="无连接" or result.status_code != 200 or len(str(result.content)) <= 0:
            print(SshLoginIp, SshLoginPort,proxies, result.status_code)
            return False
        else:
            print(SshLoginIp, SshLoginPort,proxies, 'success', result.status_code)
            return True
    except Exception as e:
        print(SshLoginIp, SshLoginPort,proxies,e)
        return False

def check(SshLoginIp, SshLoginPort,ip):
    proxies = {
        "https": "http://" + ip + ":3138"
    }
    return proxyTest(SshLoginIp, SshLoginPort,proxies)

def bohao(vps):
    try:
        with vps.work():
            vps.ssh.exec_command('pppoe-stop;pppoe-start')
            print(vps.ip,vps.port,'拨号')
    except Exception as e:
        print('拨号EC')

def execute(vpsUtil,pool):
    vpsServers = vpsUtil.queryVpsInfo()
    for (PkId, SshLoginIp, SshLoginPort, SshLoginPwd, CallIpNew, CallPort, ProxyProviderType) in vpsServers:
        vps = bsSsh.BasicSSHUtil(SshLoginIp,SshLoginPort,'root',SshLoginPwd)
        try:
            with vps.work():
                stdin, stdout, stderr = vps.ssh.exec_command(
                    'ifconfig ppp0')
                results = stdout.read()
                resultlist = str(results.decode('utf-8')).replace("b'", "").replace("'", "").strip().split("\n")
                callIPNew = ''
                for result in resultlist:
                    if 'netmask' in result:
                        callIPNew = result[result.find('inet ') + 5:result.find('netmask') - 2]
                    elif 'P-t-P:' in result:
                        callIPNew = result[result.find('addr:') + 5:result.find('P-t-P:') - 2]
                if len(callIPNew) > 1:
                    pool.run(func=check,args=(SshLoginIp, SshLoginPort,callIPNew))
                else:
                    print(SshLoginIp, SshLoginPort,'flag-',False)
        except Exception as e:
            print(SshLoginIp, SshLoginPort,'Excption-',e)
    pool.terminate()


def startJob(scheduler,second):
    pool = ThreadPoolComplex.ThreadPool(10)
    #工具
    vpsUtil = VPSServerUtil.VPSServerUtil()
    execute(vpsUtil,pool)
    #添加任务
    # scheduler.add_job(execute,"interval",seconds=second,args=[vpsUtil,])
    # #启动Job
    # scheduler.start()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    startJob(scheduler=scheduler,second=60000)