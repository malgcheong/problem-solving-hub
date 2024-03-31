# 0042
# 2579번 계단
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    stairs = [0]* (n+1)
    dp = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        stairs[i] = (int(sys.stdin.readline()))

    if n == 1:
        print(stairs[n])
    else:
        dp[1][1] = stairs[1]
        dp[1][2] = 0
        dp[2][1] = stairs[2]
        dp[2][2] = stairs[1] + stairs[2]

        for i in range(3, n+1):
            dp[i][2] = stairs[i] + dp[i-1][1]
            dp[i][1] = stairs[i] + max(dp[i-2][2], dp[i-2][1])

        print(max(dp[n][1], dp[n][2]))