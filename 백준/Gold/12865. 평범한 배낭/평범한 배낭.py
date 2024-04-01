import sys

# n은 물품 수
# k는 준서 배낭의 최대 무게
n, k = map(int, sys.stdin.readline().split())
products = []

for i in range(n):
    # w는 물품의 무게, v는 물품의 가치
    w, v = map(int, sys.stdin.readline().split())
    products.append((w,v))

# dp[i]는 i중량일 때 최대값
max_junseo_shoulder = 0
for w,v in products:
    max_junseo_shoulder += v
max_junseo_shoulder = max(max_junseo_shoulder, k)

dp = [0] * (max_junseo_shoulder + 1)

# 무게는 낮은순대로
# 무게가 똑같은 물품은 가치가 높은 순대로
products.sort(key=lambda x: (x[0],-x[1]))
# print(products)

for w,v in products:
    for i in range(max_junseo_shoulder, 0, -1):
        if dp[i] and i+w <= max_junseo_shoulder:
            dp[i+w] = max(dp[i+w], dp[i] + v)
    dp[w] = max(dp[w], v)
            
print(max(dp[:k+1]))