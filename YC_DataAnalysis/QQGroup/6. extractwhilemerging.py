fileDir = '../YCdata/csdnsplit'

fileList = []
for i in range(1,10):
    fileList.append(fileDir+'/csdn'+str(i)+'.txt')

allGroupFile = open('../YCdata/csdnalllite.txt','wb')

for filePath in fileList:
    print(filePath)
    tmpFile = open(filePath,'rb')
    tmpList = tmpFile.readlines()

    for line in tmpList:
        line = line.decode('utf-8','ignore') #二进制与文本之间的编码解码
        #print(line)
        lineList = line.split(' # ') #切割
        #print(lineList)  # ['ab','agg','ggg']q
        if len(lineList)== 3:
            GroupID=lineList[1].replace('\'','')
            GroupName = lineList[2].replace('\'','')
            #GroupTitle =lineList[6].replace('\'','')
            #抓取重要数据，替换符号
            wLine = GroupID +'\t'+GroupName
        allGroupFile.write(wLine.encode('utf-8'))

allGroupFile.close()
