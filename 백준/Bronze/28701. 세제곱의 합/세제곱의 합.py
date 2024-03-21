n = int(input())

sum = 0
for i in range(n):
    sum += i + 1

sumTwo = sum ** 2

sumThree = 0
for i in range(n):
    sumThree += (i + 1) ** 3

print(sum)
print(sumTwo)
print(sumThree)