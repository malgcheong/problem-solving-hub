import sys 
vertex = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

network = [[0] * (vertex + 1) for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)
for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    network[a][b] = network[b][a] = 1

def dfs(result, stack):
    if not stack:
        return result

    node = stack.pop()
    visited[node] = True
    result.add(node)
    for i in range(vertex+1):
        if not visited[i] and network[node][i]:
            stack.append(i)

    return dfs(result, stack)

stack = [1]
result = dfs(set(), stack)
print(len(result)-1)