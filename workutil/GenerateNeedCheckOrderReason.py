#生成需要进行订单验证的正则条件   APP-WEB同时下单

#失败原因
msg = '存在未完成订单,需要换账号重试吗?'

#正则表达式 信息
regularMsg = ""

#前缀
regularMsg += ".*"

#遍历 拼接
for ms in msg:
    regularMsg += "[" + ms + "]"

#后缀
regularMsg += ".*"

#打印最终结果
print(regularMsg)