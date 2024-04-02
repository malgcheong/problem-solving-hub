import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    pellindrome = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    seList = []
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        s,e = map(int, sys.stdin.readline().split())
        seList.append((s,e))

    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if i > j:
                break
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                if pellindrome[i-1] == pellindrome[j-1]:
                    dp[i][j] = 1
            elif j - i > 1:
                if pellindrome[i-1] == pellindrome [j-1] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1

    for s,e in seList:
        print(dp[s][e])