def merge(myList1,myList2):
    listAll =[]
    i = 0
    j = 0
    while i < len(myList1) and j < len(myList2):
        if myList1[i] < myList2[j]:
            listAll.append(myList1[i])
            i+=1

        elif myList1[i] > myList2[j]:
            listAll.append(myList2[j])
            j+=1
        else:
            listAll.append(myList1[i])
            i+=1
            listAll.append(myList2[j])
            j+=1
    while i < len(myList1):
        listAll.append(myList1[i])
        i+=1

    while j < len(myList2):
        listAll.append(myList2[j])
        j += 1

    return listAll


myList1 = [5,7,6,7,8,1,3]
myList2 = [2,4,2,6,10,8,2,2,1]
myList1.sort()
myList2.sort()
print(merge(myList1,myList2))

