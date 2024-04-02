import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        coins = list(map(int, sys.stdin.readline().split()))
        total = int(sys.stdin.readline())

        dp = [0] * (total+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(total, 0, -1):
                count = total // coin
                while True:
                    if count == 0:
                        break
                    if 0 <= i-coin*count <= total:
                        dp[i] += dp[i-coin*count]
                    count -= 1

        print(dp[total])