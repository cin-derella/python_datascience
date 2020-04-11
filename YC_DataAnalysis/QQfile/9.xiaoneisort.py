renrenPath = '../YCdata/csdnindexsort.txt'
renrenPath = '../YCdata/renrensplit/renren__0.txt'
renrenPath = '../YCdata/renrensplit/renren__1.txt'

renrenFile = open(renrenPath,'rb')
renrenList= renrenFile.readlines()
renrenFile.close()
print('read')
renrenList.sort(key = lambda x : x.decode('gbk','ignore'))
print('sort')

renrenSortPath = '../YCdata/csdnindexsorrenren.txt'
renrenSortPath = '../YCdata/renrensplit/renren__1sort.txt'
renrenSortFile = open(renrenSortPath,'wb')
for line in renrenList:
    renrenSortFile.write(line)
renrenSortFile.close()
print('save')
