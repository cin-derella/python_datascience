csdnFilePath =  '../YCdata/csdnsortbyuser.txt'
csdnIndexFilePath =  '../YCdata/csdnsortbyuserindex.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    lineNum = eval(input('Input lines :'))
    csdnIndexFile.seek(10 * (lineNum-1),0)
    lineEval = csdnIndexFile.read(10)
    lineEval = eval(lineEval)  # turn to  int

    csdnFile.seek(lineEval,0)
    line = csdnFile.readline()
    line = line.decode('gbk','ignore')
    print(line)

csdnIndexFile.close()
csdnFile.close()