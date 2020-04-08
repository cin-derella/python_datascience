import time

def costTime(args):  
    def _costTime(func):
        def __constTime(name):
            startTime = time.time()
            print('start', args)
            func(name)
            endTime = time.time()
            print('end',args)
            print(endTime - startTime, args)
        return __constTime
    return _costTime


@costTime('Disk')
def diskSearch(name):
    print('disk search', name)
    time.sleep(5)

@costTime('MEM')
def memSearch(name):
    print('mem search', name)
    time.sleep(5)

diskSearch('Shirley')
memSearch('Eric')