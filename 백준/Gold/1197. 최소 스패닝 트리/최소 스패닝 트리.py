import sys
v, e = map(int, sys.stdin.readline().split())

parentNode = [i for i in range(v+1)]
linkedList = []


for i in range(e):
    
    a,b,c = map(int, sys.stdin.readline().split())
    linkedList.append([c,a,b])

linkedList.sort()
# print(linkedList)

def find(vertex):
    global parentNode
    if parentNode[vertex] != vertex:
        return find(parentNode[vertex])
    return parentNode[vertex]

def union(u,v):
    u = find(u)
    v = find(v)
    if parentNode[u] < parentNode[v]:
        parentNode[v] = parentNode[u]
    elif parentNode[u] > parentNode[v]:
        parentNode[u] = parentNode[v]

result = 0
for i in range(len(linkedList)):
    a = linkedList[i][1]
    b = linkedList[i][2]
    c = linkedList[i][0]
    if find(a) != find(b):
        union(a,b)
        result += c

print(result)
# print(parentNode)