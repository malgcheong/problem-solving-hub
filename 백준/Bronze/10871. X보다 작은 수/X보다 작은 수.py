n,a = map(int, input().split())

list = list(map(int,input().split(maxsplit=n-1)))

for i in list:
    if i < a:
        print(i, end=' ')