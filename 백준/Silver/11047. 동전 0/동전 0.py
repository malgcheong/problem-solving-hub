import sys
n, k = map(int, sys.stdin.readline().split())

# n 10
# k 4200
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

cnt = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    cur_coin = a[i]
    cnt += k//cur_coin
    k %= cur_coin

print(cnt)
