
filePath = '../YCdata/csdnalllite.txt'
dataFile = open(filePath,'rb')
while True:
    searchStr = input('Please type keywords: ')
    dataFile.seek(0,0)
    while True:
        line = dataFile.readline()
        if not line:
            break
        else:
            line = line.decode('utf-8')
            if line.find(searchStr) != -1: 
                print(line,end = '')


dataFile.close()