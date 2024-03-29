# 10:48
# 가장 처음과 마지막 문자는 숫자이다.
# 5자리를 넘기는 연속하는 수는 없다.


# 1. 제일 작은 음수를 찾고
# 2. 제일 작은 음수 오른쪽에 +인 놈까지 합하자

import sys
inputStr = list(map(str, sys.stdin.readline().rstrip().split('-'))) 
# print(inputStr)

result = 0
for i in range(len(inputStr)):
    if i == 0 and inputStr[i] == '':
        continue
    elif i == 0 and '+' in inputStr[i]:
        str = map(int, inputStr[i].split('+'))
        result += sum(str)
    elif i == 0 and '+' not in inputStr[i]:
        result += int(inputStr[i])
    elif '+' in inputStr[i]:
        str = map(int, inputStr[i].split('+'))
        result += -sum(str)
        # print(sum(str))
    else:
        result -= int(inputStr[i])

print(result)