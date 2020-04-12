filePath = '../YCdata/csdnalllite.txt'
groupFile = open(filePath,'rb')

lengthList = [0]
while True:
    line = groupFile.readline()  # 一行一行读入
    if not line:
        break
    else:
        lengthList.append(len(line))



i =0
length = len(lengthList)
while i< length-1:
    lengthList[i+1] += lengthList[i]
    i+=1
del lengthList[length-1]

saveFilePath = '../YCdata/csdnalllite_index_disk1.txt'
saveFile = open(saveFilePath,'wb')
for data in lengthList:
    saveFile.write(format(data,'15d').encode('utf-8'))

saveFile.close()
groupFile.close()
