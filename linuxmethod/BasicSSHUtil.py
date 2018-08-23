import paramiko
import contextlib

class BasicSSHUtil(object):

    ip = ""
    port = 0
    username = ""
    password = ""
    ssh = paramiko.SSHClient()

    def __init__(self,ip,port,username,password):
        self.ip=ip
        self.port=port
        self.username=username
        self.password=password

    def before(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip,port=self.port,username=self.username,password=self.password,timeout=100)
        #print(self.ip,"连接创建")

    def after(self):
        self.ssh.close()

    @contextlib.contextmanager
    def work(self):
        self.before()
        try:
            yield
        except:
            pass
        finally:
            #print(self.ip,"连接关闭")
            self.after()