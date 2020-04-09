def getuser(line):
    line = line.decode('gbk','ignore')
    lineList = line.split(' # ')
    #print(lineList[0])
    return lineList[0]

inputFilePath = '../YCdata/csdnindexsort.txt'
outputFilePath =  '../YCdata/csdnsortbyuser.txt'

csdnInputFile = open(inputFilePath,'rb')
csdnList = csdnInputFile.readlines()
csdnInputFile.close()
print('Read Over')

csdnList.sort(key=lambda x: getuser(x))
print('Sort Over')
csdnOutputFile = open(outputFilePath,'wb')
for line in csdnList:
    csdnOutputFile.write(line)
csdnOutputFile.close()
print('Save Over')