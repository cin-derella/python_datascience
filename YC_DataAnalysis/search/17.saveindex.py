def getuser(num):
    csdnInputFile.seek(num, 0)
    line = csdnInputFile.readline()
    line = line.decode('gbk', 'ignore')
    lineList = line.split(' # ')
    return lineList[0]

filePath = '../YCdata/csdnindexsort.txt'
csdnInputFile = open(filePath, 'rb')
csdnList = csdnInputFile.readlines()

lengthList = [0]
for line in csdnList:
    lengthList.append(len(line))
del csdnList

i = 0
length = len(lengthList)
while i < length -1:
    lengthList[i+1] += lengthList[i]  # data overlay to get positions
    i += 1
del lengthList[len(lengthList)-1] #delete the last one

lengthList.sort(key=lambda x: getuser(x))  # sort index
print('Index Over')

indexFilePath =  '../YCdata/csdnsortindexnew.txt'
saveIndexfile = open(indexFilePath,'wb')
for i in range(len(lengthList)-1):
    saveIndexfile.write(format(lengthList[i],'10d').encode('utf-8'))

saveIndexfile.close()
