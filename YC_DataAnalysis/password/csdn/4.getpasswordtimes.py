csdnPassFileSortPath = '../YCdata/csdnpasstinysort.txt'
passSortFile = open(csdnPassFileSortPath,'rb')

mylist = passSortFile.readlines()
passSortFile.close()
print('read over')

savePasswordTimesFilePath = '../YCdata/csdnpasstinysorttimes.txt'
savePasswordTimesFile = open(savePasswordTimesFilePath,'wb')

length = len(mylist)
print(length)



i = 0
while i < length:
    times = 1
    password = mylist[i].decode('utf-8')
    while i+1 <= length - 1 and \
    mylist[i].decode('utf-8') == mylist[i+1].decode('utf-8'):
        times += 1
        i += 1
    savePasswordTimesFile.write((str(times)+' '+password).encode('utf-8'))
    i += 1
    #print(times,password)

savePasswordTimesFile.close()
