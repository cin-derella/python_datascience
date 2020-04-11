# 6428632

fileLinesList = [3000000,3428632]
print(fileLinesList)
filePath = '../YCdata/csdnindexsort.txt'
fileDir = '../YCdata/renrensplit'
allFile = open(filePath,'rb')
for i in range(len(fileLinesList)):
    tmpFilePath = fileDir + '/renren__' + str(i)+'.txt'
    print(tmpFilePath)
    tmpFile = open(tmpFilePath,'wb')
    for j in range(fileLinesList[i]):
        line = allFile.readline()
        tmpFile.write(line)
    tmpFile.close()
allFile.close()
