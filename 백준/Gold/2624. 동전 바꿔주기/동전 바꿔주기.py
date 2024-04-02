import sys

if __name__ == "__main__":

    t = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    coins = []
    
    for i in range(k):
        coin,count = map(int, sys.stdin.readline().split())
        coins.append((coin,count))

    dp = [0] * (t+1)
    dp[0] = 1
    temp = dp.copy()
    
    for coin,count in coins:
        for i in range(1, count+1):
            if coin * i > t:
                break
            for j in range(1, t+1):
                if 0 <= j- coin * i <= t:
                    temp[j] += dp[j-coin*i]
                
        for i in range(1, t+1):
            if temp[i]:
                dp[i] += temp[i]    
                temp[i] = 0  

    print(dp[t])