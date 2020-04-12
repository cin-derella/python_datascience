
filePath = '../YCdata/csdnindexsort.txt'
file = open(filePath,'rb')
print(file.readline())  # print one line and see how it is separated

linelList = file.readline().decode('utf-8').split('\t')
for data in linelList:
    data = data.replace('\'','')
    print(data)



file.close()