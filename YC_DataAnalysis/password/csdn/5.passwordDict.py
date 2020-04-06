passwordTimesFilePath = '../YCdata/csdnpasstinysorttimes.txt'
passwordTimesFile = open(passwordTimesFilePath,'rb')

mylist = passwordTimesFile.readlines()
passwordTimesFile.close()
print('read over')
print(mylist)  #[b'1 02365415325\n', b'1 05157538076jjj\n', b'1 1q2w3edearbook\n']
passwordTimesList = []
for line in mylist:
    line = line.decode('utf-8')
    tmplist = line.split(' ')
    passwordTimesList.append(tmplist)
print(passwordTimesList)
print('extract over')
passwordTimesList.sort(key = lambda x : int(x[0]))
passwordTimesList.reverse()
print('sort over')

saveDictFilePath = '../YCdata/csdnpasstinysorttimesdict.txt'
saveDictFile= open(saveDictFilePath,'wb')
for tmplist in passwordTimesList:
    saveDictFile.write((tmplist[0] + ' ' +tmplist[1]).encode('utf-8'))
saveDictFile.close()

print('over')
