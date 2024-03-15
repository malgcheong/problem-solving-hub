n = int(input())

allList = []
averageList = []
for i in range(n):
    allList.append(list(map(int, input().split())))

    
for list in allList:
    sum = 0
    average = 0
    del list[0]
    for i in list:
        sum += i
    average = sum / len(list)

    num = 0
    for i in list:
        if average < i:
            num += 1

    result = float(num / len(list)*100)
    print(round(result,3),'%',sep='')
