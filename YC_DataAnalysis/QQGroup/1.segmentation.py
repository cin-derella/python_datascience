import jieba

myStr1 = '我今天与朋友黄北京聊天聊到了美女与野兽'
myStr = '我是一个软件工程师，毕业于软件工程专业，从事工程软件'
myCut = jieba.cut(myStr)
print(','.join(myCut))
print(','.join(jieba.cut(myStr)))
print(','.join(jieba.cut(myStr,cut_all=True)))
print(','.join(jieba.cut(myStr,cut_all=False)))
print(','.join(jieba.cut_for_search(myStr)))