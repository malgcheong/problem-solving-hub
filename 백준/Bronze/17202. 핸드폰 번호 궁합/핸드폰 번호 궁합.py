import sys
st1 = list(map(int, sys.stdin.readline().rstrip()))
st2 = list(map(int, sys.stdin.readline().rstrip()))

compat = []
for i in range(8):
    compat.append(st1[i])
    compat.append(st2[i])



while len(compat) != 2:
    for i in range(len(compat)-1):
        compat[i] = (compat[i] + compat[i+1]) % 10
    compat = compat[0:len(compat)-1]


print(str(compat[0]) + str(compat[1]))
