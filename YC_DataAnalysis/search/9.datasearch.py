import time


def costTime(func):
    def _costTime(findData, findList):
        startTime = time.time()
        func(findData, findList)
        endTime = time.time()
        print(endTime - startTime)

    return _costTime


@costTime
def search(findData, findList):
    for data in findList:
        if data == findData:
            print('find', data)
            return
    print('not find')


@costTime
def search2(findData, findList):
    low = 0  # first index number
    high = len(findList) - 1  # last index number

    times = 0
    while low <= high:
        times += 1
        print('times:', times)
        mid = (low + high) // 2  # middle index number
        midData = findList[mid]  # middle index value
        if findData < midData:  # elininate half of index
            high = mid - 1
        elif findData > midData:
            low = mid + 1
        else:
            print('find', findData, mid)
            return mid
    print('not find')
    return -1


@costTime
def search2lr(findData, findList):
    low = 0  # first index number
    high = len(findList) - 1  # last index number

    times = 0
    while low <= high:
        times += 1
        print('times:', times)

        #mid = (low + high) // 2  # middle index number
        #mid = int(low + (high - low) * 0.5)
        dataMid =((findData-low)/(high-low))
        # dataMid = 0.5
        mid = int(low+(high-low)* dataMid)

        midData = findList[mid]  # middle index value
        if findData < midData:  # elininate half of index
            high = mid - 1
        elif findData > midData:
            low = mid + 1
        else:
            print('find', findData, mid)
            return mid
    print('not find')
    return -1


findList = [x for x in range(100000000)]
# findData = 98009999+0.1
while True:
    findData = eval(input('data'))
    #search(findData, findList)
    search2lr(findData, findList)
