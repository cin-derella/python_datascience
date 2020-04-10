


csdnFilePath =  '../YCdata/csdnindexsort.txt'
csdnIndexFilePath =  '../YCdata/csdnsortindexnew.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    searchStr = input('Input searchStr:')
    search2(searchStr)



csdnIndexFile.close()
csdnFile.close()