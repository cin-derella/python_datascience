filePath = '../YCdata/renrensplit/renren__1sort.txt'
QQFile = open(filePath,'rb')
i = 0
while True:
    line = QQFile.readline()
    if i%1000000 == 0:  #read every 100w line
        print(i)
    if not line:
        break
    else:
        i+=1
print('end = ', i)
QQFile.close()