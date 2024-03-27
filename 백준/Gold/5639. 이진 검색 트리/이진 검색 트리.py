import sys

sys.setrecursionlimit(10**6)
tree = []
while True:
    try:
        num = int(sys.stdin.readline())
        tree.append(num)
    except:
        break


def binarySearchTree(s,e):
    if s > e:
        return
    if s == e:
        print(tree[s])
        return

    mid = e
    for i in range(s, e+1):
        if tree[s] < tree[i]:
            mid = i-1
            break
    
    binarySearchTree(s+1, mid)
    binarySearchTree(mid+1, e)
    print(tree[s])

binarySearchTree(0, len(tree)-1)
