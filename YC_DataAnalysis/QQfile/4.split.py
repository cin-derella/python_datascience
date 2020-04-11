#100
#[10,10,10,10,10,10,10,10,10,10,]

#97
#[10,10,10,10,10,10,10,10,10,7]
# 97-97%10 =90 /9
def evgSplit(num,N):
    lastList = []
    if num%N == 0:
        for i in range(N):
            lastList.append(num//N)
    else:
        evg = (num-num%N)//(N-1)
        for i in range(N-1):
            lastList.append(evg)
            num-=evg
        lastList.append(num)
    return lastList


print(evgSplit(100,10))
print(evgSplit(103,10))
print(evgSplit(97,10))
print(evgSplit(6428632,10))
#num = 6428632