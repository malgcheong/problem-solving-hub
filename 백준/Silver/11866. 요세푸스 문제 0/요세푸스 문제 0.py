import sys
from collections import deque

# n명
# k번째 사람 제거
# n명이 사람이 모두 제거될때 까지
# 사람 제거되는 순서를 (N,K)-요세푸스 순열

# 예시
# (7,3) - 요세푸스 순열은 <3,6,2,7,5,1,4>
#1 2 3 4 5 6 7
#1 2 x 4 5 6 7 -> 3
#1 2 x 4 5 x 7 -> 3,6
#1 x x 4 5 x 7 -> 3,6,2
# ~

#1 2 3 4 5 6 7
#3 4 5 6 7 1 2
#4 5 6 7 1 2    -> 3
#6 7 1 2 4 5    
#7 1 2 4 5      -> 3,6
#2 4 5 7 1 
#4 5 7 1        -> 3,6,2
# ~

# for문 n-1번 하기
# k-1 번 왼쪽으로 회전
# popleft
# k-1 번 왼쪽으로 회전
# popleft
# ~

n, k = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, n+1)])
result = []
while len(dq) != 0:
    for _ in range(k-1):
        dq.append(dq.popleft())

    # dq.rotate(-k+1)
    result.append(str(dq.popleft()))



print(f"<{', '.join(result)}>")