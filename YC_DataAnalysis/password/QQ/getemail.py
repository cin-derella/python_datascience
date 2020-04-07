import re

filePath = '../YCdata/QQ通讯录.txt'
filePathUtf8 = '../YCdata/QQUtf8.txt'
tencentFile = open(filePath,'rb')
lastText = tencentFile.read()  # read() returns bytes type
print(type(lastText))
tencentFile.close()


lastText = lastText.decode('gb2312','ignore')
print(type(lastText))  # decode() returns  a str type
lastTextUtf8 = lastText.encode('utf-8')
print(type(lastTextUtf8))  # encode() returns  a bytes type

tencentFileUtf8 = open(filePathUtf8, 'wb')
# tencentFileUtf8.write(lastText)  # Incorrect ,write() could write bytes type only, not string type
tencentFileUtf8.write(lastTextUtf8) # Correct
tencentFileUtf8.close()

regexEmail = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})',re.IGNORECASE)
mailList = regexEmail.findall((lastText))
print(type(mailList))  # mailList is list type
for mail in mailList:
    print(mail)

