class CSDNFind:
    def __init__(self,csdnFilePath,csdnIndexFilePath):
        self.csdnFile = open(csdnFilePath, 'rb')
        self.csdnIndexFile = open(csdnIndexFilePath, 'rb')


    def search2(self,searchStr):
        low = 0  # first index number
        high = 6428632 - 1  # last index number


        while low <= high:
            mid = (low + high) // 2  # middle index number

            self.csdnIndexFile.seek(10 * (mid - 1), 0)
            lineEval = self.csdnIndexFile.read(10)
            lineEval = eval(lineEval)  # turn to  int

            self.csdnFile.seek(lineEval, 0)
            line = self.csdnFile.readline()
            line = line.decode('gbk', 'ignore')
            lineList = line.split(' # ')
            midData = lineList[0]

            if searchStr < midData:  # eliminate half of index
                high = mid - 1
            elif searchStr > midData:
                low = mid + 1
            else:
                return True,line
        return False,None


    def findline(self,searchstr):
        pass

    def __del__(self):
        self.csdnIndexFile.close()
        self.csdnFile.close()


csdnFilePath =  '../YCdata/csdnindexsort.txt'
csdnIndexFilePath =  '../YCdata/csdnsortindexnew.txt'

csdn = CSDNFind(csdnFilePath,csdnIndexFilePath)
print(csdn.search2('yincheng01'))
print(csdn.search2('yincheng'))
