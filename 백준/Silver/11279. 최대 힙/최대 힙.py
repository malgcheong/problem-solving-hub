import heapq
import sys

n = int(sys.stdin.readline())
hq = []

for i in range(n):
    cmd = int(sys.stdin.readline())
    if cmd  == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
    elif cmd != 0:
        heapq.heappush(hq, -cmd)
    