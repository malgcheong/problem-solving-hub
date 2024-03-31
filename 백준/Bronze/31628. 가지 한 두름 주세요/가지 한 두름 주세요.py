import sys
boards = [sys.stdin.readline().rstrip().split() for _ in range(10)]
cnt = 0
for i in range(10):
    init_color = boards[i][0]
    flg = 0
    for color in boards[i][1:]:
        if color == init_color:
            flg += 1
    if flg == 9:
        cnt = 1
for i in range(10):
    init_color = boards[0][i]
    flg = 0
    for color in [boards[j][i]  for j in range(1, 10)]:
        if color == init_color:
            flg += 1
    if flg == 9 :
        cnt = 1
print(cnt)