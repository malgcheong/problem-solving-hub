
list = [int(input()) for _ in range(9)]
n = len(list)
suspectList = []
answerList = []

for i in range(n):
    for j in range(i+1, n):
        if [i,j] not in suspectList:
            suspectList.append([i,j])

for i in range(len(suspectList)):
    print
    suspect1 = suspectList[i][0]
    suspect2 = suspectList[i][1]
    if sum(list) - list[suspect1] - list[suspect2] == 100:
        list.remove(list[suspect2])
        list.remove(list[suspect1])
        break

list.sort()

[print(li) for li in list]
