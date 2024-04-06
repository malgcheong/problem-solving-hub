import sys
t = int(sys.stdin.readline())

for _ in range(t):

    n,m = map(int, sys.stdin.readline().split())
    cnt = 0
    ans = 1
    for i in range(1, n):
        for j in range(i+1, n):
            if (i**2 + j**2 + m) % (i*j) == 0:
                cnt += 1
        
    print(cnt)
        