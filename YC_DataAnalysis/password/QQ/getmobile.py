import re

filePath = '../YCdata/QQ通讯录.txt'
tencentFile = open(filePath,'rb')
lastText = tencentFile.read()  # read() returns bytes type
print(type(lastText))
tencentFile.close()


lastText = lastText.decode('gb2312','ignore')
regexEmail = re.compile('1[34578]\d{9}',re.IGNORECASE)
mobileList = regexEmail.findall((lastText))
for mobile in mobileList:
    print(mobile)