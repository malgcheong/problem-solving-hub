import sys
t = int(sys.stdin.readline())

for _ in range(t):

    n,m = map(int, sys.stdin.readline().split())
    ansList = []
    ans = 1
    for i in range(1, n):
        for j in range(1, n):
            if i < j:
                ans = (i**2 + j**2 + m) % (i*j)
            else:
                ans = 1
            
            if ans == 0:
                ansList.append((i,j))
        
    print(len(ansList))
        