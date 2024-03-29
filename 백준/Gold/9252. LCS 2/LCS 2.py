# 9252번 LCS2
# 23:00 ~ 23:34
import sys

def findLCS(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            elif s1[j-1] != s2[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    count = dp[m][n]
    result = []
    y = m
    x = n
    while len(result) != count:
        if dp[y][x] == dp[y-1][x]:
            y = y-1
        elif dp[y][x] == dp[y][x-1]:
            x = x-1
        else:
            y = y-1
            x = x-1
            result.append(s1[x])

    result = result[::-1]
    return (count, result)


a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

count, result = findLCS(a,b)

if result:
    print(count,''.join(result), sep="\n")
else:
    print(count)