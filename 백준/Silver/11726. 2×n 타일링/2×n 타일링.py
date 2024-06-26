import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dp = [0] * (1001)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1]%10007 + dp[i-2]%10007)%10007

    print(dp[n])