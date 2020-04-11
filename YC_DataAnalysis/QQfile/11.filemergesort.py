# 1 lines 3000000
# 2 lines 3428632


path1 = '../YCdata/renrensplit/renren__0sort.txt'
path2 = '../YCdata/renrensplit/renren__1sort.txt'
mergePath =  '../YCdata/renrenmergesort.txt'
file1 = open(path1,'rb')
file2 = open(path2,'rb')

fileLast = open(mergePath,'wb')
file1Length = 3000000
file2Length = 3428632

i = 0
j = 0
str1 = file1.readline()
str2 = file2.readline()
lineStr1 = str1.decode('gbk','ignore')
lineStr2 = str2.decode('gbk','ignore')

while i < file1Length and j <file2Length:
    if lineStr1 < lineStr2:
        fileLast.write(str1)
        str1 = file1.readline()
        lineStr1 = str1.decode('gbk','ignore')
        i+=1

    elif lineStr1 > lineStr2:
        fileLast.write(str2)
        str2 = file2.readline()
        lineStr2 = str2.decode('gbk', 'ignore')
        j += 1
    else:
        fileLast.write(str1)
        str1 = file1.readline()
        lineStr1 = str1.decode('gbk','ignore')
        i+=1

        fileLast.write(str2)
        str2 = file2.readline()
        lineStr2 = str2.decode('gbk', 'ignore')
        j += 1

while i < file1Length:
    fileLast.write(str1)
    str1 = file1.readline()
    i+=1


while j < file1Length:
    fileLast.write(str2)
    str2 = file2.readline()
    j+=1


file1.close()
file2.close()
fileLast.close()