def search2(searchStr):
    low = 0  # first index number
    high = 6428632 -1   # last index number

    times = 0
    while low <= high:
        times += 1
        print('times:', times)
        mid = (low + high) // 2  # middle index number

        csdnIndexFile.seek(10 * (mid - 1), 0)
        lineEval = csdnIndexFile.read(10)
        lineEval = eval(lineEval)  # turn to  int

        csdnFile.seek(lineEval, 0)
        line = csdnFile.readline()
        line = line.decode('gbk', 'ignore')
        lineList = line.split(' # ')
        midData = lineList[0]


        if searchStr < midData:  # eliminate half of index
            high = mid - 1
        elif searchStr > midData:
            low = mid + 1
        else:
            print('find', line, mid)
            return mid
    print('not find')
    return -1

csdnFilePath =  '../YCdata/csdnsortbyuser.txt'
csdnIndexFilePath =  '../YCdata/csdnsortbyuserindex.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    searchStr = input('Input searchStr:')
    search2(searchStr)



csdnIndexFile.close()
csdnFile.close()