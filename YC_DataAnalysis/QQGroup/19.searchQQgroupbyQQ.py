def search2(searchStr):
    low = 0  # first index number
    high = 5714340 -1   # last index number


    while low <= high:
        mid = (low + high) // 2  # middle index number

        csdnIndexFile.seek(15 * (mid - 1), 0)
        lineEval = csdnIndexFile.read(15)
        lineEval = eval(lineEval)  # turn to  int

        csdnFile.seek(lineEval, 0)
        line = csdnFile.readline()
        line = line.decode('utf-8', 'ignore')
        lineList = line.split('\t')
        midData = lineList[0]
        #midData = eval(midData)


        if searchStr < midData:  # eliminate half of index
            high = mid - 1
        elif searchStr > midData:
            low = mid + 1
        else:
            #print('find', mid,line)
            QQList = []
            QQList.append(line)  #返回一个列表，多个QQ，先加入找到的第一个

            tmp_up = mid #循环向上查找
            while True:
                tmp_up-=1 #循环向上
                if tmp_up < low: #不可以低于下限
                    break
                if tmp_up-1 <0:
                    break
                #索引文件取出位置tmp_up
                csdnIndexFile.seek(15 * (tmp_up - 1), 0)
                uplineEval = csdnIndexFile.read(15)
                uplineEval = eval(uplineEval)  # turn to  int

                #根据索引文件在文件中的位置uplinelist[0]群号
                csdnFile .seek(uplineEval, 0) #根据索引取出位置
                upline = csdnFile.readline()
                upline = upline.decode('utf-8', 'ignore')
                uplineList = upline.split('\t')
                upmidData = uplineList[0]

                if searchStr == upmidData: #相等继续，不等跳出循环
                    #print(upline,tmp_up)
                    QQList.append(upline)
                else:
                    break

            tmp_down = mid #向下循环
            while True:
                tmp_down+=1 #向下移动
                if tmp_down> high: #不能高于上限
                    break
                #索引文件取出tmpdown
                csdnIndexFile.seek(15 * (tmp_down - 1), 0)
                downlineEval = csdnIndexFile.read(15)
                downlineEval = eval(downlineEval)  # turn to  int
                #根据索引文件取出downlinelist【0】
                csdnFile.seek(downlineEval, 0)
                downline = csdnFile.readline()
                downline = downline.decode('utf-8', 'ignore')
                downlineList = downline.split('\t')
                downmidData = downlineList[0]

                if searchStr == downmidData:
                    #print(downline, tmp_down)
                    QQList.append(downline)
                else:
                    break

            return QQList
    print('not find')
    return -1

csdnFilePath =  '../YCdata/csdnalllite.txt'
csdnIndexFilePath =  '../YCdata/csdnalllite_index.txt'
csdnFile = open(csdnFilePath,'rb')
csdnIndexFile = open(csdnIndexFilePath,'rb')


while True:
    searchStr = input('Input searchStr:')
    QQList = search2(searchStr)

    for QQLine in QQList:
        print(QQLine,end='')


csdnIndexFile.close()
csdnFile.close()