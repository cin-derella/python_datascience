filePath = '../YCdata/csdnalllite.txt'
groupFile = open(filePath,'rb')
groupList = groupFile.readlines()  # 土豪版，全部载入内存
print(len(groupList))

lengthList = [0]
for line in groupList:
    lengthList.append(len(line))
i =0
length = len(lengthList)
while i< length-1:
    lengthList[i+1] += lengthList[i]
    i+=1
del lengthList[length-1]


saveFilePath = '../YCdata/csdnalllite_index.txt'
saveFile = open(saveFilePath,'wb')
for data in lengthList:
    saveFile.write(format(data,'15d').encode('utf-8'))

saveFile.close()
groupFile.close()


'''
def getuser(num):
    groupFile.seek(num, 0)
    line = groupFile.readline()
    line = line.decode('gbk', 'ignore')
    lineList = line.split('\t')
    return lineList[0]

lengthList = [0]
for line in groupList:
    lengthList.append(len(line))
i =0
length = len(lengthList)
while i< length-1:
    lengthList[i+1] += lengthList[i]
    i+=1
del lengthList[length-1]

lengthList.sort(key= lambda x: getuser(x))
saveFilePath = '../YCdata/csdnalllite_index.txt'
saveFile = open(saveFilePath,'wb')
for data in lengthList:
    saveFile.write(format(data,'15d').encode('utf-8'))

saveFile.close()
groupFile.close()
'''