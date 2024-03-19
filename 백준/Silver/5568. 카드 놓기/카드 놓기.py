import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]
cachedList = []
answerList = []
checkList = [False] * n
count = 0


def combination():
    if len(cachedList) == k:
        answer = ''.join(map(str, cachedList))
        global count
        if answer not in answerList:
            answerList.append(answer)
        count += 1
        return

    for i in range(n):
        if not checkList[i]:
            checkList[i] = True
            cachedList.append(cards[i])
            combination()
            checkList[i] = False
            cachedList.pop()
        
combination()

# print(count)
# print(answerList)
print(len(answerList))
