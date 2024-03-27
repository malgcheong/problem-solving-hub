from collections import deque

def bfs(n, k):
    visited = [False] * 100001
    queue = deque([(n, 0)])  # 시작 지점과 현재까지의 시간을 저장하는 큐
    visited[n] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            return time
        
        # 걷는 경우, 순간이동 하는 경우 각각 확인
        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())
result = bfs(n, k)
print(result)