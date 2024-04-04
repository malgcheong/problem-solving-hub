import sys

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]

# print(dp[0][0][0])
def recursive(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        if not dp[a+50][b+50][c+50]:
            dp[a+50][b+50][c+50] = 1
        return dp[a+50][b+50][c+50]

    elif a > 20 or b > 20 or c > 20:
        if not dp[70][70][70]:
            dp[70][70][70] = recursive(20, 20, 20)
        return dp[70][70][70]
    
    elif a < b and b < c:
        if not dp[a+50][b+50][c+49]:
            dp[a+50][b+50][c+49] = recursive(a, b, c-1)
        if not dp[a+50][b+49][c+49]:
            dp[a+50][b+49][c+49] = recursive(a, b-1, c-1)
        if not  dp[a+50][b+49][c+50]:
            dp[a+50][b+49][c+50] = recursive(a, b-1, c)
        return dp[a+50][b+50][c+49] + dp[a+50][b+49][c+49] - dp[a+50][b+49][c+50]

    else:
        if not dp[a+49][b+50][c+50]:
            dp[a+49][b+50][c+50] = recursive(a-1, b, c)
        if not dp[a+49][b+49][c+50]:
            dp[a+49][b+49][c+50] = recursive(a-1, b-1, c)
        if not dp[a+49][b+50][c+49]:
            dp[a+49][b+50][c+49] = recursive(a-1, b, c-1)
        if not dp[a+49][b+49][c+49]:
            dp[a+49][b+49][c+49] = recursive(a-1, b-1, c-1)        
        return dp[a+49][b+50][c+50] + dp[a+49][b+49][c+50] + dp[a+49][b+50][c+49] - dp[a+49][b+49][c+49]

while True:
        a,b,c = map(int, sys.stdin.readline().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f"w({a}, {b}, {c}) = {recursive(a,b,c)}")

