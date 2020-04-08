def come(func):
    print('come up')
    func()
    print('come down')

def go(func):
    print('go up')
    func()
    print('go down')
    return func

@come # come(go(printdata)
@go  # @go  go(printdata)
def printdata():
    print('1234')
