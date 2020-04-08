def toadd(func):
    def _toadd(a,b):
        print('go up')
        func(a,b)
        print('go down')
    return _toadd

def toaddplus(func):
    def _toadd(*arg):
        print('go up')
        func(*arg)
        print('go down')
    return _toadd

@toaddplus
def add(a,b,c):
    print(a,b,c)
    return a+b+c

add(1,2,3)
