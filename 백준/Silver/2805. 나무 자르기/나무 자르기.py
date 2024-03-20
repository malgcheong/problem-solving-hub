# n = 5
# m = 20
# trees = [4, 42, 40, 26, 46]
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

def cuttingTrees(meter):

    # 최소값은 0
    # 최대값은 trees[-1]
    
    left = 0
    right = trees[-1]

    while left <= right:
        cuttingTree = 0
        pivot = (left + right) // 2

        for i in range(len(trees)):
            if(trees[i] > pivot):
                cuttingTree += trees[i] - pivot
        
        # pivot을 늘려서 더 적게 나무를 얻어야 해
        # 그러기 위해선 기존 피봇을 left에 넣어야 해
        if cuttingTree >= meter:
            result = pivot
            left = pivot + 1

        # pivot을 줄여서 더 많은 나무를 얻어야 해
        # 그러기 위해선 기존 피봇을 right에 넣어야 해
        elif cuttingTree < meter:
            right = pivot - 1
        
    return result

print(cuttingTrees(m))