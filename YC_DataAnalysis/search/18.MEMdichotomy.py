def search2(searchStr, lengthList):
    low = 0  # first index number
    high = len(lengthList) - 1  # last index number

    times = 0
    while low <= high:
        times += 1
        print('times:', times)
        mid = (low + high) // 2  # middle index number

        midIndex = lengthList[mid]
        csdnInputFile.seek(midIndex, 0)
        line = csdnInputFile.readline()  # read line
        line = line.decode('gbk', 'ignore ')
        lineList = line.split(' # ')
        midData = lineList[0]

        if searchStr < midData:  # elininate half of index
            high = mid - 1
        elif searchStr > midData:
            low = mid + 1
        else:
            print('find', line, mid)
            return mid
    print('not find')
    return -1


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
while i < length - 1:
    lengthList[i + 1] += lengthList[i]  # data overlay to get positions
    i += 1
del lengthList[len(lengthList) - 1]  # delete the last one

lengthList.sort(key=lambda x: getuser(x))  # sort index
print('Index Over')

while True:
    searchStr = input('Input data :')
    search2(searchStr,lengthList)

csdnInputFile.close()
