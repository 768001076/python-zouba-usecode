# 删除其他格式的文件
import os

# 删除操作
def del_files(path):
    # 切换目录
    os.chdir(path)
    print(os.listdir(path))

# test
if __name__ == "__main__":
    path = r'D:\UPclas\offline_refund_kt'
    del_files(path)