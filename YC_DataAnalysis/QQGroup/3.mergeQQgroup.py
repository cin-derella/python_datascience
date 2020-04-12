import os

fileDir = '../../../filedir'
fileNameList  = os.listdir(fileDir)
print(fileNameList)

fileList = []
for i in range(1,111):
    fileList.append(fileDir+'/QQGroup'+str(i)+'.txt')

allFile = open('QQGroup1.0.txt','wb')


for filePath in fileList:
    print(filePath)
    tmpFile = open(filePath,'rb')
    tmpList = tmpFile.readlines()
    for line in tmpFile:
        allFile.write(line)

'''
    while True:
        line = tmpFile.readline()
        if not line:
            break
        else:
            allFile.write()
    tmpFile.close()
'''


allFile.close()