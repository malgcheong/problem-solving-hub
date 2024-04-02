import sys

if __name__ == '__main__':

    n,k = map(int,sys.stdin.readline().split())
    coins = []

    for _ in range(n):
        coins.append(int(sys.stdin.readline()))

    dp = [float('inf')] * (k+1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(1, k+1):
            if 0 <= i - coin <= k:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[k] == float('inf'):
        print(-1)
    else:
        print(dp[k])