csdnFilePath =  '../YCdata/csdnalllite.txt'
csdnIndexFilePath =  '../YCdata/csdnalllite_index.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    lineNum = eval(input('Input lines :'))
    csdnIndexFile.seek(15 * (lineNum-1),0)
    lineEval = csdnIndexFile.read(15)
    lineEval = eval(lineEval)  # turn to  int

    csdnFile.seek(lineEval,0)
    line = csdnFile.readline()
    line = line.decode('utf-8','ignore')
    print(line)

csdnIndexFile.close()
csdnFile.close()