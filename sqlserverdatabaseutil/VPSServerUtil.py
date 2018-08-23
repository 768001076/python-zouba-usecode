#REP工具类
from sqlserverdatabaseutil import SQLServerBaseUtil

class VPSServerUtil(object):

    sql_server = None

    def __init__(self):
        self.sql_server = SQLServerBaseUtil.SQLServerBaseUtil(host='120.55.85.58',db='B2B_DB_TC')

    def queryVpsInfo(self):
        with self.sql_server.exec():
            if self.sql_server.conn_success:
                res = self.sql_server.query('select PkId,SshLoginIp,SshLoginPort,SshLoginPwd,CallIpNew,CallPort,ProxyProviderType from vpsrepserverinfo WHERE ProxyProviderType IN (2)')
                return res

    def UpdateVpsInfo(self,Pkid,state):
        with self.sql_server.exec():
            if self.sql_server.conn_success:
                sql = 'update vpsrepserverinfo set State=' + str(state) + ',UpdateTime=GETDATE() Where PkId=' + str(Pkid)
                print(sql)
                self.sql_server.execute(sql )


if __name__ == '__main__':
    vpsUtil = VPSServerUtil()
    vpsServers = vpsUtil.queryVpsInfo()
    for (PkId,SshLoginIp,SshLoginPort,SshLoginPwd,CallIpNew,CallPort) in vpsServers:
        print(PkId)