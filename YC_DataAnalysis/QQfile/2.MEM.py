import time
filePath = '../YCdata/csdnindexsort.txt'
csdnFile = open(filePath,'rb')
myList = csdnFile.readlines()
print('load')
csdnFile.close()
time.sleep(100)
print(len(myList))

