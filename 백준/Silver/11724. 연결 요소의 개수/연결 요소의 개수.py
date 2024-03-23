import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

v, e = map(int, sys.stdin.readline().split())
connectedVertex = [i for i in range(1, v+2)]
visited = [False] * (v+1)

class graph():

    def __init__(self):
        # self.linkedList = {}
        self.linkedList = defaultdict(list)

    def addEdge(self, u, v):
        # if u not in self.linkedList:
        #     self.linkedList[u] = []
        # if v not in self.linkedList:
        #     self.linkedList[v] = []
        self.linkedList[u].append(v)
        self.linkedList[v].append(u)
        
    def dfs(self, stack):
        if not stack:
            return
        node = stack.pop()
        if visited[node] == False:
            visited[node] = True
            connectedVertex.remove(node)
            stack.extend(sorted(self.linkedList[node], reverse=True))
        return self.dfs(stack)
        
graph = graph()

for i in range(e):
    u, v = map(int, sys.stdin.readline().split())
    graph.addEdge(u,v)

stack = []
stack.append(connectedVertex.pop())
count = 0
while connectedVertex:
    stack = []
    stack.append(connectedVertex[0])
    graph.dfs(stack)
    count += 1

print(count)