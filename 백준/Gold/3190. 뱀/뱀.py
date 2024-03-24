import sys
from collections import deque
n = int(sys.stdin.readline())

# 보드 생성
board = [[0]*(n+1) for _ in range(n+1)]

k = int(sys.stdin.readline())

# 사과 배치
for i in range(k):
    u, v = map(int, sys.stdin.readline().split())
    board[u][v] = 1

# 뱀이 머리 방향을 바꾼대 ㄷㄷ
# 동서남북으로만 바꿀수있네 ㅋㅋ 바보
direction = {}
l = int(sys.stdin.readline())
for i in range(l):
    u, v = map(str, sys.stdin.readline().split())
    direction[int(u)] = v

# [print(*b) for b in board] 

# 시간
time = 0

# 뱀 위치
snake = deque()

# 이동방법 (오른쪽, 왼쪽, 아래쪽, 위쪽)
moveX = [0, 0, 1, -1] 
moveY = [1, -1, 0, 0]

# 뱀 초반 위치
snake.append([1,1])

# 종료조건
# 스네이크가 벽이 부딪히거나
# 스네이크가 자기 몸에 부딪히거나
# deque 클리어하거나 break로 종료
# 뱀의 기본방향을 알아야 left,right할 때 어디로 이동할지 알 수 있다.
snakeHead = 'E'
while snake:

    # # 1초에 한 번 뱀 이동
    # time += 1 

    # 우선은 오른쪽 이동
    # 먼저 머리를 들이넣고
    head = snake[-1]

    # 뱀 이동
    if time in direction.keys():
        if snakeHead == 'E':
            if direction[time] == "L":
                snakeHead = 'N'
            elif direction[time] == "D":                
                snakeHead = "S"
        elif snakeHead == 'S':
            if direction[time] == "L":
                snakeHead = 'E'
            elif direction[time] == "D":
                snakeHead = "W"
        elif snakeHead == 'W':
            if direction[time] == "L":
                snakeHead = 'S'
            elif direction[time] == "D":
                snakeHead = "N"
        elif snakeHead == 'N':
            if direction[time] == "L":
                snakeHead = 'W'
            elif direction[time] == "D":
                snakeHead = "E"

    if snakeHead == 'E':
        newX = head[0] + moveX[0]
        newY = head[1] + moveY[0]
    elif snakeHead == 'S':
        newX = head[0] + moveX[2]
        newY = head[1] + moveY[2]                
    elif snakeHead == 'W':
        newX = head[0] + moveX[1]
        newY = head[1] + moveY[1]                
    elif snakeHead == 'N':
        newX = head[0] + moveX[3]
        newY = head[1] + moveY[3]                
    # 만약 머리 들이민 곳이 벽이라면?
    # 만약 머리 들이민 곳이 애석하게도 자기 몸이면?
    # print(f"{newX}, {newY}")
    if 1 <= newX <= n and 1 <= newY <= n and [newX,newY] not in snake:
        # 1초에 한 번 뱀 이동
        time += 1 
        # 그게 아니라면 머리를 집어넣으삼
        snake.append([newX,newY])
        # 만약 머리 들이민 곳이 사과가 없다면 
        if board[newX][newY] != 1:
            # 꼬리를 빼고
            snake.popleft()
        elif board[newX][newY] == 1:
        # 사과가 있다면 꼬리를 빼지마라!
        # 그리고 사과를 먹어치워라
            board[newX][newY] = 0

    else:
        time+=1
        break

print(f"{time}")

    