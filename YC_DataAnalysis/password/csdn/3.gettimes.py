
mylist = [1111,2222,2222,2222,3333,3333,4444,4444,5566]
length = len(mylist)
i=0
while i<length:
    times = 1
    password = mylist[i] # save the original pwd
    while i+1 <= length -1 and mylist[i] == mylist[i+1]:
        times += 1
        i += 1

    print(times, password)
    i = i + 1