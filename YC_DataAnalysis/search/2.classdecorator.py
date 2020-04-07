import time

class costTime:
    def __init__(self,func):
        startTime = time.time()
        func()
        endTime = time.time()
        print(endTime - startTime)

@costTime
def go():
    num = 0
    for i in range(100000000):
        num += i
    print(num)
