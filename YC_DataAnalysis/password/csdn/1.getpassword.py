csdnFilePath = '../YCdata/csdntiny.txt'
csdnPassFilePath = '../YCdata/csdnpasstiny.txt'
passFile = open(csdnPassFilePath,'wb')
file = open(csdnFilePath, 'rb')

#count = 0
while True:
    line = file.readline()
    #count += 1
    if not line:
        break
    line = line.decode('gbk', 'ignore')
    line = line.strip('\r\n')

    linelist = line.split(' # ')
    #print(linelist)
    #print(linelist[1])
    passFile.write((linelist[1]+'\n').encode('utf-8'))
passFile.close()
file.close()
print('over')
