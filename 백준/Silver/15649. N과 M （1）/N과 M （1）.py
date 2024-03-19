n, m = map(int,input().split())
inputList = [i+1 for i in range(n)]
chkList = [0] * n
answerList = []

def dfs(idx, answer):

    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(len(inputList)):

        if not chkList[i]:
            answer.append(i+1)
            chkList[i] += 1

            dfs(i+1, answer)

            answer.pop()
            chkList[i] -= 1


dfs(0, [])
