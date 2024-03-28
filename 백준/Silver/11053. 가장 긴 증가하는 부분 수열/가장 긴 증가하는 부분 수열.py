import sys

n = int(sys.stdin.readline())

sequence = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(len(sequence)):
    for j in range(0, i):
        if sequence[j] < sequence[i]:
                dp[i] = max(dp[j] + 1, dp[i]) 
print(max(dp))