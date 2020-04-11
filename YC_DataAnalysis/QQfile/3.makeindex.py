def getuser(num):
    csdnInputFile.seek(num, 0)
    line = csdnInputFile.readline()
    line = line.decode('gbk', 'ignore')
    lineList = line.split(' # ')
    if len(lineList) == 3:
        return lineList[0]
    else:
        return ''

filePath = '../YCdata/csdnindexsort.txt'
csdnInputFile = open(filePath, 'rb')
csdnList = csdnInputFile.readlines()

lengthList = [0]
for line in csdnList:
    lengthList.append(len(line))
del csdnList
print('read')

i = 0
length = len(lengthList)
while i < length -1:
    lengthList[i+1] += lengthList[i]  # data overlay to get positions
    i += 1
del lengthList[len(lengthList)-1] #delete the last one
print('get')
lengthList.sort(key=lambda x: getuser(x))  # sort index
print('Index Over')

indexFilePath =  '../YCdata/csdnsortindexQQ.txt'
saveIndexfile = open(indexFilePath,'wb')
for i in range(len(lengthList)-1):
    saveIndexfile.write(format(lengthList[i],'15d').encode('utf-8'))

saveIndexfile.close()
