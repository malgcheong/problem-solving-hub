import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
v,e,s = map(int, sys.stdin.readline().split())
visited = [False] * (v+1)
visited2 = visited.copy()


class graph():
    def __init__(self):
        self.linkedList = defaultdict(list)

    # 간선 추가 함수
    def add_edge(self, u, v):
        self.linkedList[u].append(v)
        self.linkedList[v].append(u)

    def dfs(self, start):
        stack = [start]
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                print(node, end=" ")
                stack.extend(sorted(self.linkedList[node], reverse=True))

        
    def bfs(self, start):
        dq = deque([start])
        
        while dq:
            node = dq.popleft()
            if not visited2[node]:
                visited2[node] = True
                print(node, end=' ')
                dq.extend(sorted(self.linkedList[node], reverse=False))

graph = graph()

for i in range(e):
    u, v = map(int, sys.stdin.readline().split())
    graph.add_edge(u,v)

graph.dfs(s)
print()
graph.bfs(s)
print()
