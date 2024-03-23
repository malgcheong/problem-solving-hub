import sys
from collections import deque
sys.setrecursionlimit(10**6)

v, e, s = map(int, sys.stdin.readline().split())

graph = [[0] * (v+1) for _ in range(v+1)]
visited = [0] * (v + 1)
visited2 = visited.copy()

for _ in range(1, e+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] =graph[b][a] = 1

def dfs(stack):
    if not stack:
        print()
        return 
    node = stack.pop()
    if visited[node] == 0:
        print(node, end=' ')
    visited[node] = 1 
    for i in range(v, 0, -1):
        if not visited[i] and graph[node][i]:
            stack.append(i)
    dfs(stack)

def bfs(queue):
    if not queue:
        print()
        return
    node = queue.popleft()
    if visited2[node] == 0:
        print(node, end=' ')
    visited2[node] = 1
    for i in range(1, v+1):
        if not visited2[i] and graph[node][i]:
            queue.append(i)
    bfs(queue)
    
stack = [s]
dq = deque([s])

dfs(stack)
bfs(dq)
