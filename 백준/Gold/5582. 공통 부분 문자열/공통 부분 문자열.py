import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = list(sys.stdin.readline().rstrip())

len_str1 = len(str1)
len_str2 = len(str2)
dp = [[0] * (len_str1+1) for _ in range(len_str2+1)]

max_count = 0
for i in range(1, len_str2+1):
    for j in range(1, len_str1+1):
        if str2[i-1] == str1[j-1]:
            # print(f"{i=} {j=}")
            dp[i][j] = dp[i-1][j-1] + 1

        if dp[i][j] > max_count:
            max_count = dp[i][j]

print(max_count)