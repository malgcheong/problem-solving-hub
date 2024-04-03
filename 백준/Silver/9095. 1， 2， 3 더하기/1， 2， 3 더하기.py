import sys

t = int(sys.stdin.readline())

for i in range(t):    
    n = int(sys.stdin.readline())

    dp = [0] * 12
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] += dp[i-1] + dp[i-2] + dp[i-3]
            
    print(dp[n])
