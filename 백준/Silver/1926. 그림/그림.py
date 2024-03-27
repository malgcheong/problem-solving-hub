import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
areaList = []
dq = deque()

direction = [(0,1), (1,0), (0,-1), (-1,0)]

for k in range(n):
    for l in range(m):
        if paper[k][l] == 1 and  not visited[k][l]:
            dq.append((k,l))
            area = 0
            while dq:
                x, y = dq.popleft()
                area += 1
                if not visited[x][y]:
                    visited[x][y] = 1
                newX, newY = 0,0
                for i in range(4):
                    newX = x + direction[i][0]
                    newY = y + direction[i][1]
                    if 0 <= newX < n and 0 <= newY < m:
                        if not visited[newX][newY] and paper[newX][newY] == 1:
                            visited[newX][newY] = visited[x][y] + 1
                            dq.append((newX,newY))
            areaList.append(area)

cnt = 0
for i in visited:
    for j in i:
        # print(j, end="")
        if j == 1:
            cnt+=1
    # print()
    
print(cnt)
if areaList:
    print(max(areaList))
else:
    print(0)