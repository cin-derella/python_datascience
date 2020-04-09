filePath =  '../YCdata/csdnsortbyuser.txt'

csdnInputFile = open(filePath,'rb')
csdnList = csdnInputFile.readlines()

lengthList=[0]
for line in csdnList:
    lengthList.append(len(line))  #read every line to  lengthList


i = 0
length = len(lengthList)
while i < length -1:
    lengthList[i+1] += lengthList[i]  # data overlay to get positions
    i += 1


indexFilePath =  '../YCdata/csdnsortbyuserindex.txt'
saveIndexfile = open(indexFilePath,'wb')
for i in range(len(lengthList)-1):
    saveIndexfile.write(format(lengthList[i],'10d').encode('utf-8'))

saveIndexfile.close()
csdnInputFile.close()