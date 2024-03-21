# 3시 50분까지
# 0 을 부르면 pop
import sys
k = int(input())
stack = []

for i in range(k):

    n = int(sys.stdin.readline())
    if(n == 0):
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))