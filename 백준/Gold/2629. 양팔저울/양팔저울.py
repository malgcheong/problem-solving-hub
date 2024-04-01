import sys

n = int(sys.stdin.readline())
pendulum = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
bead = list(map(int, sys.stdin.readline().split()))

dp = [False] * 40001
temp = set()
for p in pendulum:
    for i in range(len(dp)-1,0,-1):
        if dp[i]:
            # print(i + p)
            # print(abs(i - p))
            # dp[i + p] = True
            # dp[abs(i - p)] = True
            temp.add(i+p)
            temp.add(abs(i-p))

    for t in temp:
        if t <= 40000:
            dp[t] = True 
    dp[p] = True

for b in bead:
    if dp[b]:
        print("Y", end=" ")
    else:
        print("N", end=" ")