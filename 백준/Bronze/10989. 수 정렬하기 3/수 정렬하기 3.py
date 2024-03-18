import sys
MAX_NUM = 10001

inputList = [0] * MAX_NUM
# countList = [0] * MAX_NUM
# answerList = [0] * MAX_NUM

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    inputList[num] += 1

for i in range(len(inputList)):
    if inputList[i]:
        for _ in range(inputList[i]):
            print(i)
            