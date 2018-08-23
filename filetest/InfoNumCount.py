#计数
countInfo = {}
log = open('C:\\Users\\Administrator\\Desktop\\log\\AccountGet.log', 'r')
for line in log:
    try:
        countInfo[line.strip()] = countInfo[line.strip()] + 1
    except:
        countInfo[line.strip()] = 1
print(countInfo)