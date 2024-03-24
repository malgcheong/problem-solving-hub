from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
visited = [False] *  (n+1)
result = [0] * (n+1)

class graph():
    def __init__(self):
        self.linkedList = defaultdict(list)

    def addEdge(self, u, v):
        self.linkedList[u].append(v)
        self.linkedList[v].append(u)

    def dfs(self, stack):

        if not stack:
            return

        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            temp = list(self.linkedList[node])
            for t in temp:
                if not visited[t]:
                    result[t] = node
            stack.extend(sorted(self.linkedList[node], reverse=True))

        self.dfs(stack)
        return
        

gp = graph()

while True:
    try:
        u, v = map(int, sys.stdin.readline().split())
        gp.addEdge(u,v)
    except:
        break

stack = [1]
gp.dfs(stack)
for r in result[2:]:
    print(r)