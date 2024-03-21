# 3시 30분까지
import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push':
        value = command[1]
        stack.append(int(value))

    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    elif command[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

