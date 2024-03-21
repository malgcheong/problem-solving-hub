import sys
from collections import deque

# 한 장 버리고
# 그 다음 한장을 제일 아래에 있는 카드 밑으로 옮긴다.
# 1 2 3 4
# 2 3 4
# 3 4 2
# 4 2
# 2 4
# 4 

n = int(sys.stdin.readline())
dq = deque([i for i in range(1, n+1)])

for i in range(len(dq)-1):

    dq.popleft()
    dq.rotate(-1)
    

print(dq[0])