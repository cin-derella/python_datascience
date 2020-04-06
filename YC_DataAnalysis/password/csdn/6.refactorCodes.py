inputPath = '../YCdata/csdntiny.txt'
outputPath = '../YCdata/csdnlast.txt'
inputFile = open(inputPath,'rb')
outputFile = open(outputPath,'wb')

allLineList = inputFile.readlines()  #read all
print('read over')

passwordList = []
for line in allLineList:
    line = line.decode('gbk','ignore')
    lineList = line.split(' # ')
    if len(lineList) == 3:
        passwordList.append(lineList[1])  # add pwd to list

del allLineList # clean memory, wont user allLineList again
print('extract over')

passwordList.sort()
print('sort over')

passwordTimesList = []  #[3,'abc']
length = len(passwordList)
i = 0
while i < length:
    times = 1
    password = passwordList[i]
    while i+1 <= length - 1 and passwordList[i] == passwordList[i+1]:
        times +=1
        i+=1
    passwordTimesList.append([password,times])
    i+=1

del passwordList
print('count over')

passwordTimesList.sort(key = lambda x : x[1])
passwordTimesList.reverse()
print('times sort over')

for line in passwordTimesList:
    outputFile.write((str(line[0]) + ' ' + str(line[1]) + '\n').encode('utf-8'))
print('write over')



inputFile.close()
outputFile.close()
