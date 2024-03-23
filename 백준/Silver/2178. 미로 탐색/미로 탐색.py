# 09:50
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
miro = []
moveX = [0, 0, 1, -1]
moveY = [1, -1, 0, 0]
dq = deque()

for i in range(n):
    miro.append([0] * m)
    input = sys.stdin.readline().strip()
    for j in range(m):
        miro[i][j] = int(input[j])

dq.append((0,0))

def bfs(miro, dq):
    while dq:
        po = dq.popleft()
        x = po[0]
        y = po[1]
        for i in range(4):
            newX = po[0]+moveX[i]
            newY = po[1]+moveY[i]
            if newX >= 0 and newY >= 0 and newX < len(miro) and newY < len(miro[0]):
                newPo = miro[newX][newY]
                if newPo == 1:
                    dq.append((newX, newY))
                    miro[newX][newY] = miro[x][y] + 1


bfs(miro, dq)
print(miro[n-1][m-1])
