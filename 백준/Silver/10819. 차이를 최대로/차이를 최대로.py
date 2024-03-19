n = int(input())
inputList = list(map(int,input().split()))
tempDict = {}
tempList = []
answerList = []

def dfs():
    if len(tempDict) == n:
        sum = 0
        tempList = list(tempDict.values())
        for i in range(len(tempList)-1):
            sum += abs(tempList[i+1] - tempList[i])

        answerList.append(sum)
        return 

    for i in range(0, len(inputList)):
        if i not in tempDict.keys():
            tempDict[i] = inputList[i]
            dfs()
            tempDict.pop(i)

dfs()
print(max(answerList))