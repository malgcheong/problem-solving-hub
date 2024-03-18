# n장의 카드는 최소 3장부터
# 3장의 카드만
# n, m = 10, 500
# cardList = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
n, m = map(int,input().split())
cardList = list(map(int,input().split()))
cheatkey = []
answerList = [] 

def dfs(cardIndex:int, depth:int) -> None:
    if(depth == 3):
        if sum(cheatkey) <= m:
            answerList.append([value for value in cheatkey])
            return False
        else: return False

    for i in range(cardIndex, len(cardList)):
        if list[i] not in cheatkey:
            cheatkey.append(cardList[i])

        flag = dfs(i + 1, depth + 1)
        if not flag:
            cheatkey.pop()
        else:
            return True

dfs(0 ,0)

answer = [sum(answer) for answer in answerList]
print(max(answer))

