def getpassword():
    yield 1
    yield 2
    yield 3

T  = getpassword()
print((next(T)))
print((next(T)))
print((next(T)))
print('hello')
