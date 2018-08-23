#代理不可用异常信息分析
import ast
import json
ExceptionInfos = {}
for i in range(1):
    file = open("C:\Users\Administrator\Desktop\proxy" + str(i) + ".log","r")
    lines = file.readlines()
    for line in lines:
        exceinfo = ast.literal_eval(line.split(",jsonStr:")[1])
        for exec in exceinfo.keys():
            messageinfo = exceinfo[exec]
            if exec in ExceptionInfos.keys():
                for message in messageinfo.keys():
                    if message in ExceptionInfos[exec].keys():
                        ExceptionInfos[exec][message] = ExceptionInfos[exec][message] + messageinfo[message]
                    else:
                        ExceptionInfos[exec][message] = messageinfo[message]
            else:
                ExceptionInfos[exec] = messageinfo
    print("C:\Users\Administrator\Desktop\proxy" + str(i) + ".log")

print(json.dumps(ExceptionInfos))