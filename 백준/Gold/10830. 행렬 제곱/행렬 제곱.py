import sys
n, b = map(int, sys.stdin.readline().split())
procession =[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def multiProcession(a, b):
    global n
    multiList = [[0] * n for _ in range(n)]

    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(n):
                multiList[i][j] += a[i][k] * b[k][j]
            multiList[i][j] %= 1000
    return multiList

def multiProcessionRecursive(square, result):
    if square == 1:
        for i in range(n):
            for j in range(n):
                result[i][j] %= 1000
        return result

    if square % 2 == 0:
        halfResult = multiProcessionRecursive(square//2, result)
        return multiProcession(halfResult, halfResult)

    elif square % 2 == 1:
        halfResult = multiProcessionRecursive(square//2, result)
        return multiProcession(multiProcession(halfResult, halfResult), result )

answerList = multiProcessionRecursive(b, procession)
for i in range(n):
    for j in range(n):
        print(answerList[i][j], end=" ")
    print()
