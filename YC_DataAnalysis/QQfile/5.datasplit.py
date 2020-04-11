def evgSplit(num, N):
    lastList = []
    if num % N == 0:
        for i in range(N):
            lastList.append(num // N)
    else:
        evg = (num - num % N) // (N - 1)
        for i in range(N - 1):
            lastList.append(evg)
            num -= evg
        lastList.append(num)
    return lastList


fileLinesList = evgSplit(6428632, 10)
print(fileLinesList)
filePath = '../YCdata/csdnindexsort.txt'
fileDir = '../YCdata/csdnsplit'
allFile = open(filePath,'rb')
for i in range(len(fileLinesList)):
    tmpFilePath = fileDir + '/csdn' + str(i)+'.txt'
    print(tmpFilePath)
    tmpFile = open(tmpFilePath,'wb')
    for j in range(fileLinesList[i]):
        line = allFile.readline()
        tmpFile.write(line)
    tmpFile.close()
allFile.close()
