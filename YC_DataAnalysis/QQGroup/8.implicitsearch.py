import jieba
import jieba.posseg

def findData(myStr,lastStr):
    jiebaStr = ','.join(jieba.cut(myStr,cut_all=True))
    wordList  = jiebaStr.split(',')

    length = len(wordList)
    getLength = 0
    for word in wordList:
        if lastStr.find(word)!= -1:
            getLength+=1
    return getLength/length  # 返回相关性




filePath = '../YCdata/csdnalllite.txt'
dataFile = open(filePath,'rb')

dataList = dataFile.readlines()
print('load MEM')

while True:
    searchStr = input('Please type keywords: ')
    dataFile.seek(0,0)

    for line in dataList:
            line = line.decode('utf-8')
            #if line.find(searchStr) != -1:
            if findData(searchStr,line) >= 0.3:
                print(line,end = '')


dataFile.close()