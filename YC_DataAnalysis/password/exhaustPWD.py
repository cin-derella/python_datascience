# _ _ _ _  1 2 3 4
# 4*4*4*4

import itertools
mylist = ["".join(x) for x in itertools.product("1234",repeat = 4)]
print(len(mylist))

# taobao password
mylist1 = ["".join(x) for x in itertools.product("0123456789",repeat = 6)]
print(len(mylist1))


for line in mylist:
     print(line)