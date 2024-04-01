import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
vocaes = []

for i in range(n):
    vocaes.append(sys.stdin.readline().rstrip())
len_s = len(s)
dp = [False] * (len_s+1)
dp[0] = True
for i in range(1, len_s+1):
    for voca in vocaes:
        len_voca = len(voca)
        # print(i-len_voca, i)
        # print(s[i-len_voca:i])
        if len_voca <= len_s and s[i-len_voca:i] == voca:
            # print('test')
            dp[i] = dp[i] | dp[i-len_voca]

if dp[len_s]:
    print(1)
else:
    print(0)