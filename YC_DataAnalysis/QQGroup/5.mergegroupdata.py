fileDir = '../YCdata/cdsnsplit'

fileList = [] # 文件列表
for i in range(1,111):
    fileList.append(fileDir+'/QQGroup'+str(i)+'.txt') # 批量生成110个文件，加入文件列表
# 用于归并
allGroupFile = open('../YCdata/csdnall.txt','wb')
# 每个文件读取1次，每个文件写入归并文件，
for filePath in fileList:
    print(filePath)
    tmpFile = open(filePath,'rb') #打开文件
    tmpList = tmpFile.readlines() #读取所有行
    for line in tmpFile: #所有文件的行，批量写入归并
        allGroupFile.write(line)

allGroupFile.close()
