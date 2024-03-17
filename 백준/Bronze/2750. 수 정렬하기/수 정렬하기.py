import sys
list = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

for i in range(len(list)):
    for j in range(i+1, len(list)):

        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

[print(v) for v in list]