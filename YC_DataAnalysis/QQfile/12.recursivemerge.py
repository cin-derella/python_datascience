import os

dir = '../YCdata/csdnsplit'
fileNameList  = os.listdir(dir)
# print(fileNameList)

def getLast(myList):
    if len(myList) < 2:
        print(myList)
        return myList
    else:
        myList.append(myList[0] + myList[1])
        print(myList)

        del myList[0]
        del myList[0]
        print(myList)
        getLast(myList)


def getLastX(myList):
    if len(myList) < 2:
        print(myList)
        return myList
    else:
        n = len(myList)//2
        for i in range(n):
            myList.append(myList[2*i]+myList[2*i+1])
            print(myList)
        for i in range(n):
            del myList[0]
            del myList[0]
        print(myList)
        getLastX(myList)



myList = ['1','2','3','4','5','6','7','8','9','0']
getLastX(myList)

