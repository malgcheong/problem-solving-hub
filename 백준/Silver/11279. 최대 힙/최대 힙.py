#17:00
# 최대 힙
import sys
from collections import deque
n = int(sys.stdin.readline())

maxHeap = deque()
def switchNodeFadd(me):
    parent = me // 2
    if parent == 0:
        return
    
    if maxHeap[me-1] > maxHeap[parent-1]:
        maxHeap[me-1], maxHeap[parent-1] = maxHeap[parent-1], maxHeap[me-1]
        switchNodeFadd(parent)
    else:
        return

def switchNodeFdelete(me):
    left = me * 2 
    right = me * 2 + 1

    if len(maxHeap) < left:
        return
    elif len(maxHeap) == left:
        if maxHeap[left-1] > maxHeap[me-1]:
            maxHeap[me-1], maxHeap[left-1] = maxHeap[left-1], maxHeap[me-1]
        return
        
    if maxHeap[left-1] >= maxHeap[right-1]:
        if maxHeap[left-1] > maxHeap[me-1]:
            maxHeap[me-1], maxHeap[left-1] = maxHeap[left-1], maxHeap[me-1]
        switchNodeFdelete(left)

    elif maxHeap[left-1] <= maxHeap[right-1]:
        if maxHeap[right-1] > maxHeap[me-1]:
            maxHeap[me-1], maxHeap[right-1] = maxHeap[right-1], maxHeap[me-1]
        switchNodeFdelete(right)
    
    else:
        return

for i in range(n):

    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if not maxHeap:
            print(0)
        else:
            max = maxHeap.popleft()
            print(max)

            if maxHeap:
                max2 = maxHeap.pop()
                maxHeap.appendleft(max2)
                switchNodeFdelete(1)

                
    elif cmd != 0:
        maxHeap.append(cmd)
        node = len(maxHeap)
        switchNodeFadd(node)
