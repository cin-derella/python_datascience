'''
filePath = '../YCdata/csdnsplit/csdn0.txt'
file = open(filePath,'rb')
#print(file.readline())  # print one line and see how it is separated

linelList = file.readline().decode('utf-8').split(' # ')
for data in linelList:
    data = data.replace('\'','')
    print(data)
file.close()
'''

fileDir = '../YCdata/cdsnsplit'

fileList = [] # 文件列表
for i in range(1,10):
    fileList.append(fileDir+'/csdn'+str(i)+'.txt') # 批量生成110个文件，加入文件列表
# 用于归并
allGroupFile = open('../YCdata/csdnall.txt','wb')
# 每个文件读取1次，每个文件写入归并文件，
for filePath in fileList:
    print(filePath)
    tmpFile = open(filePath,'rb') #打开文件
    tmpList = tmpFile.readlines() #读取所有行
    for line in tmpFile: #所有文件的行，批量写入归并
        lineList = line.split('\t')
        QQ = lineList[1].replace('\'', '')
        QQName = lineList[2].replace('\'', '')
        QQAge = lineList[3].replace('\'', '')
        QQGroup = lineList[6].replace('\'', '')
        wline = QQ + '\t' + QQName + '\t'+QQAge+'\t'+QQGroup  #最后一个不用加\t

        allGroupFile.write(wline.encode('utf-8'))

allGroupFile.close()

