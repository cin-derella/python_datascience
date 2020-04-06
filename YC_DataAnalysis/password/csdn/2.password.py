
csdnPassFilePath = '../YCdata/csdnpasstiny.txt'
passFile = open(csdnPassFilePath,'rb')

myPassList = passFile.readlines()
passFile.close()
print('read over')
myPassList.sort()
print(('sort over'))


csdnPassFileSortPath = '../YCdata/csdnpasstinysort.txt'
passSortFile = open(csdnPassFileSortPath,'wb')
for line in myPassList:
    passSortFile.write(line)
passSortFile.close()
print('write over') 