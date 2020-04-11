def merge(myList1,myList2):
    listAll =[]
    while len(myList1)> 0  and len(myList2) > 0:
        if myList1[0] < myList2[0]:
            listAll.append(myList1[0])
            del myList1[0]
        elif myList1[0] > myList2[0]:
            listAll.append(myList2[0])
            del myList2[0]
        else:
            listAll.append(myList1[0])
            del myList1[0]
            listAll.append(myList2[0])
            del myList2[0]
    listAll.extend(myList2)
    listAll.extend(myList1)

    return listAll


myList1 = [5,7,6,7,8,1,3]
myList2 = [2,4,2,6,10,8,2,2,1]
myList1.sort()
myList2.sort()
print(merge(myList1,myList2))

