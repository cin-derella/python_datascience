def search2(searchStr):
    low = 0  # first index number
    high = 5714340 -1   # last index number

    times = 0
    while low <= high:
        times += 1
        print('times:', times)
        mid = (low + high) // 2  # middle index number

        print(f'{mid}')
        csdnIndexFile.seek(15 * (mid - 1), 0)
        lineEval = csdnIndexFile.read(15)
        print('[' + lineEval.decode() + ']')
        lineEval = eval(lineEval)  # turn to  int

        csdnFile.seek(lineEval, 0)
        line = csdnFile.readline()
        line = line.decode('utf-8', 'ignore')
        lineList = line.split('\t')
        midData = lineList[0]
        print(lineList[0])



        if searchStr < midData:  # eliminate half of index
            high = mid - 1
        elif searchStr > midData:
            low = mid + 1
        else:
            print('find', line, mid)
            while True:
                csdnIndexFile.seek(15 * (mid), 0)
                linenextEval = csdnIndexFile.read(15)
                print('[' + linenextEval.decode() + ']')
                linenextEval = eval(linenextEval)  # turn to  int
                csdnFile.seek(linenextEval, 0)
                linenext = csdnFile.readline()
                linenext = linenext.decode('utf-8', 'ignore')
                linenextList = linenext.split('\t')
                if linenextList[0] == lineList[0]:
                    print(linenext)
                    mid += 1
                else:
                    break
            return mid
    print('not find')
    return -1

csdnFilePath =  '../YCdata/csdnalllite.txt'
csdnIndexFilePath =  '../YCdata/csdnalllite_index.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    searchStr = input('Input searchStr:')
    search2(searchStr)



csdnIndexFile.close()
csdnFile.close()