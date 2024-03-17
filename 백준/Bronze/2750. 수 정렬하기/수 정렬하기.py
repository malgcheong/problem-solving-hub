import sys
list = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

for i in range(len(list)-1):
    for j in range(1, len(list)):
        if list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]

for v in list:
    print(v)