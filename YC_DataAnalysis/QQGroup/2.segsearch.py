import jieba
import jieba.posseg

myStr = '软件工程'  # 分词分的是要搜的（搜索关键词）
lastStr = '工程软件1班' # 匹配在其中搜的
jiebaStr = ','.join(jieba.cut(myStr,cut_all=True))

print(jieba.cut(myStr,cut_all=True))
jiebaObj = jieba.cut(myStr,cut_all=True)
for i in jiebaObj:
    print(i)

print(jiebaStr)
wordList  = jiebaStr.split(',')
print(wordList)

length = len(wordList)
getLength = 0
for word in wordList:
    if lastStr.find(word)!= -1:
        getLength+=1
print(getLength/length)