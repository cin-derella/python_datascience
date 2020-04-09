filePath =  '../YCdata/csdnsortbyuser.txt'

csdnInputFile = open(filePath,'rb')
csdnList = csdnInputFile.readlines()

lengthList=[0]
for line in csdnList:
    lengthList.append(len(line))  #read every line to  lengthList
print(lengthList)

i = 0
length = len(lengthList)
while i < length -1:
    lengthList[i+1] += lengthList[i]  # data overlay to get positions
    i += 1

while True:
    lineNum = eval(input('Input lines :'))
    csdnInputFile.seek(lengthList[lineNum-1],0) # jump to certain position
    line = csdnInputFile.readline() #read line
    print(line)

csdnInputFile.close()

