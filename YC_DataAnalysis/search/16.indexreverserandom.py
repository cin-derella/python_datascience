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

i = 0
length = len(lengthList)
while i < length - 1:
    lengthList[i + 1] += lengthList[i]  # data overlay to get positions
    i += 1

lengthList.sort(key=lambda x: getuser(x))  # sort index
print('Index Over')

while True:
    lineNum = eval(input('Input lines :'))
    csdnInputFile.seek(lengthList[lineNum], 0)  # jump to certain position
    line = csdnInputFile.readline()  # read line
    print(line)
