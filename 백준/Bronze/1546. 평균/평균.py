import sys
n = int(sys.stdin.readline())

numList = list(map(int,sys.stdin.readline().split()))

max = max(numList)
temp = 0
for i in range(len(numList)):

    temp += numList[i] / max * 100

print(temp/n)