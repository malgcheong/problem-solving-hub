n = int(input())

for _ in range(n):

    inputStr = input()
    stack = []

    cnt = 0
    for str in inputStr:
        if str == '(':
            stack.append(str)
            cnt += 1
        elif str == ')':
            if len(stack) == 0:
                print("NO")
                break
            stack.pop()
            cnt += 1

    if len(stack) > 0:
        print("NO")
    elif cnt == len(inputStr):
        print("YES")

        
