import numpy as np
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
b = np.broadcast(x,y)
b.index
print(b.__next__()) #循环下一个
print(b.__next__())
print(b.__next__())
print(b.index) #索引位置