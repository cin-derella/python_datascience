from snownlp import SnowNLP

data = SnowNLP('这饭真赞')
print(data.words) #分词
print(str(data.tags)) #词性
for tag in data.tags:
    print(str(tag))

print(data.sentiments) # 情感分析
print(data.pinyin) #拼音

data = SnowNLP('表裏山河')
print(data.han)

text = '''
繁体字，也称繁体中文，欧美各国称之为“传统中文（Traditional Chinese）”，一般是指汉字简化运动被简化字所代替的汉字，有时也指汉字简化运动之前的整个汉字楷书、隶书书写系统。繁体中文至今已有三千年以上的历史，直到1956年前一直是各地华人中通用的中文的标准字。
'''
data = SnowNLP(text)
print(data.keywords(5)) #抽取文章关键字
print(data.summary(3))  #概要
print(data.sentences) #句子