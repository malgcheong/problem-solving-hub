import sys

if __name__ == '__main__':

    n,k = map(int, sys.stdin.readline().split())
    dp = [0] * (k+1)
    dp[0] = 1
    coins = []

    for _ in range(n):
        coins.append(int(sys.stdin.readline()))

    for coin in coins:
        for i in range(1, k+1):
            if coin <= i:
                dp[i] += dp[i-coin]
            # cnt = k // coin
            # while True:
            #     if cnt == 0:
            #         break
            #     if 0 <= i - coin * cnt <= k:
            #         dp[i] += dp[i-coin * cnt]
            #     cnt -= 1
    print(dp[k])