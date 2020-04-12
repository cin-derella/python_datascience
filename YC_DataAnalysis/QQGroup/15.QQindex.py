filePath = '../YCdata/csdnalllite.txt'
groupFile = open(filePath,'rb')
saveFilePath = '../YCdata/csdnalllite_index.txt'
saveFile = open(saveFilePath,'wb')

pos = 0
saveFile.write(format(pos, '15d').encode('utf-8'))

while True:
    line = groupFile.readline()  # 一行一行读入,边读编写
    if not line:
        break
    else:
        pos += len(line)

saveFile.close()
groupFile.close()
