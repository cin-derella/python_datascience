import time

filePath = '../password/YCdata/csdnindexsort.txt'

def costTime(func):
    startTime = time.time()
    func()
    endTime = time.time()
    print(endTime-startTime)


def searchMEM():
    pass


@costTime
def searchDisk():
    searchStr = input('Plesase input string you want to search:')
    csdnFile = open(filePath,'rb')
    while True:
        line = csdnFile.readline()
        if not line:
            break
        line  = line.decode('gbk','ignore')
        if line.find(searchStr) != -1:
            print(line)
    csdnFile.close()

