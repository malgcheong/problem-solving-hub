import sys
n = int(sys.stdin.readline())
bread_shop = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    bread_shop.append((a,b))

bread_shop.sort()

# 0이 내가 가는시간
# 1이 빵 나오는 시간
# 0이 1보다 늦지만 않으면 됨
stack = []
for i in range(n):
    shop = bread_shop[i]
    if shop[0] > shop[1]:
        continue
    else:
        stack.append(shop[1])

if stack:
    print(min(stack))
else:
    print(-1)