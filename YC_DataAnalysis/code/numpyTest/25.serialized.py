import numpy as np

'''
# 写入
a = np.array([1,2,3,4,5,6,7,8,9,0])
print(a)
np.save('1.txt',a)


#读取
b = np.load('1.txt.npy')
print(b)

'''

a = np.array([1,2,3,4,5,6,7,8,9,0])
np.savetxt('1.txt',a)

b= np.loadtxt('1.txt')
print(b)