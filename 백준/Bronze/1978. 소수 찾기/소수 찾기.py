n = int(input())

a = list(map(int,input().split()))

count = 0
for n in a:
    for i in range(1,n+1):
        if(i == 1):
            continue
        if(n!= i and n % i == 0):
            break
        if(i == n):
            count += 1

print(count)
    