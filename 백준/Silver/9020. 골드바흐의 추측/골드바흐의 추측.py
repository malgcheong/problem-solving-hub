
n = int(input())
list = [2]

def checkPrime(x):
    if x == 1: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(3, 10000, 2):
    for j in range(3, i+1):
        if i % j == 0 and i != j:
            break
        if i == j:
            list.append(j)

for _ in range(n):
    newList = []
    newList2 = []
    a = int(input())
    newList = [x for x in list if x < a]

    for i in newList:
        if checkPrime(a-i) and a-i >= i:
            newList2.append([a-i, i])

    print(newList2[-1][1], newList2[-1][0])
    # print(newList2)