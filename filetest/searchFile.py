file = open('C:\Users\Administrator\Desktop\filetest\1.log','r')
file2 = open('C:\Users\Administrator\Desktop\filetest\2.log','w')
lines = file.readlines()
for i in lines:
    if i.__contains__('(1,1,57,6,1)'):
        file2.write(i)