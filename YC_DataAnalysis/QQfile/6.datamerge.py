import os
fileDir = '../YCdata/csdnsplit'
print(os.listdir(fileDir))
allFilePath = '../YCdata/csdnmerge.txt'
allFile = open(allFilePath,'wb')
for filename in os.listdir(fileDir):
    print (fileDir+'//'+filename)
    tmpFile = open(fileDir+'//'+filename,'rb')
    while True:
        line = tmpFile.readline()
        if not line:
            break
        else:
            allFile.write(line)

    tmpFile.close()
allFile.close()
