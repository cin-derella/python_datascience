import time

filePath = '../password/YCdata/csdnindexsort.txt'

def costTime(func):
    startTime = time.time()
    func()
    endTime = time.time()
    print(endTime-startTime)
    return costTime,func

def loopGo(args):
    costTime,func = args
    while True:
        costTime(func)




def searchMEM():
    csdnFile = open(filePath,'rb')
    lines  = csdnFile.readlines()

    @loopGo
    @costTime
    def search():
        searchStr = input('Plesase input string you want to search(MEM):')
        for line in lines:
            line  = line.decode('gbk','ignore')
            if line.find(searchStr) != -1:
                print(line)

        csdnFile.close()

searchMEM()

@costTime
def searchDisk():
    searchStr = input('Plesase input string you want to search(DISK):')
    csdnFile = open(filePath,'rb')
    while True:
        line = csdnFile.readline()
        if not line:
            break
        line  = line.decode('gbk','ignore')
        if line.find(searchStr) != -1:
            print(line)
    csdnFile.close()

