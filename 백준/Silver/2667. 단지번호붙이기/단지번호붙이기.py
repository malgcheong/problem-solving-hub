from collections import deque
import sys
n = int(sys.stdin.readline())

miro = []

for i in range(n):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))


visited = [[0] * n for _ in range(n)]
dq = deque()
direction = [(-1,0),(1,0),(0,-1),(0,1)]
count = 0
areaList = []

for i in range(n):

    for j in range(n):

        if miro[i][j] == 1 and not visited[i][j]:
            dq.append((i,j))
            visited[i][j] = 1
            area = 0
            while dq:
                x, y = dq.popleft()
                area+=1
                for k in range(4):
                    newX = x + direction[k][0]
                    newY = y + direction[k][1]

                    if 0 <= newX < n and 0 <= newY < n:

                        if miro[newX][newY] != 0 and not visited[newX][newY]:
                            visited[newX][newY] = visited[x][y] + 1
                            dq.append((newX, newY))
            areaList.append(area)
            count += 1

print(count)
areaList.sort()
for i in areaList:
    print(i)
