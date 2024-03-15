n = int(input())

for i in range(n):
    a = list(map(str, input().split()))
    for i in a[1]:
        print(i * int(a[0]), end='')
    print("")
