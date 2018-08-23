# 链接SQL server 底层工具类
import pymssql
import contextlib


class SQLServerBaseUtil(object):
    host = ''
    port = 1433
    name = 'sa'
    password = '5n0wbIrd'
    db = ''
    timeout = 30
    login_timeout = 10
    charset = 'utf-8'

    sql_connection = None
    cursor = None
    conn_success = False

    def __init__(self, host='', port='1433', name='sa', password='5n0wbIrd', db='', timeout=30, login_timeout=10,
                 charset='utf8'):
        self.host = host
        self.port = port
        self.name = name
        self.password = password
        self.db = db
        self.timeout = timeout
        self.login_timeout = login_timeout
        self.charset = charset

    def initConnection(self):
        try:
            self.sql_connection = pymssql.connect(host=self.host, port=self.port,user=self.name, password=self.password,
                                                  database=self.db, timeout=self.timeout, login_timeout=self.login_timeout,
                                                  charset=self.charset)
            self.cursor = self.sql_connection.cursor()
            self.conn_success = True
        except Exception as e:
            self.conn_success = False
            print("初始化链接失败:",e)

    def colseMethod(self):
        if self.conn_success:
            self.cursor.close()
            self.sql_connection.close()


    @contextlib.contextmanager
    def exec(self):
        self.initConnection()
        try:
            yield
        except Exception as e:
            print("异常:",e)
        finally:
            self.colseMethod()

    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.sql_connection.commit()