# lcs
# 0920
import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

lcs = [ [0] * (len(a)+1) for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):

        if a[j-1] == b[i-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1

        elif a[j-1] != b[i-1]:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(max(max(lcs)))