# memory friendly way to get passoword

import itertools

def getpassword():
     for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz",repeat = 16):
         yield "".join(x)

T  = getpassword()
for i in range(100):
    print((next(T)))
