n = int(input())

count = 0
for i in range(1, n+1):

    chkList = []
    x = str(i)
    if(len(x) <= 2):
        count += 1
    elif(len(x) == 3):
        for j in x:
            chkList.append(j)
        chkList = list(map(int, chkList))
        if chkList[1] - chkList[0] == chkList[2] - chkList[1]:
            count += 1


print(count)
