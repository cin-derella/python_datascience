filePath = '../../../Data/project_muse_free_covid_books.txt'
file = open(filePath,'rb')

urlFile = open('../../../Data/bookurl.txt', 'wb')
lineFile = file.readlines()
#print(lineFile)
count = 0
for line in lineFile:
    count +=1
    if count == 1:
        continue
    line = line.decode('utf-8','ignore')
    lineList = line.split('\t')
    #print(lineList)

    url = lineList[9].replace('\'','')
    #print(urlList)

    urlFile.write((url+'\r\n').encode('utf-8'))



urlFile.close()
file.close()