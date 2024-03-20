# n = 8
# coloredPaper = [
    # [1, 1, 0, 0, 0, 0, 1, 1],
    # [1, 1, 0, 0, 0, 0, 1, 1],
    # [0, 0, 0, 0, 1, 1, 0, 0],
    # [0, 0, 0, 0, 1, 1, 0, 0],
    # [1, 0, 0, 0, 1, 1, 1, 1],
    # [0, 1, 0, 0, 1, 1, 1, 1],
    # [0, 0, 1, 1, 1, 1, 1, 1],
    # [0, 0, 1, 1, 1, 1, 1, 1]
    # ]

n = int(input())
coloredPaper = []

for _ in range(n):
    coloredPaper.append(list(map(int, input().split())))

whitePaper, bluePaper = 0, 0

# x = [0,3]
# y = [0,3]
def chkColoredPaper(targetN, x, y):
    global whitePaper, bluePaper
    whiteCount = 0
    for i in range(y[0], y[1]+1):
        for j in range(x[0], x[1]+1):
            if coloredPaper[i][j] == 0:
                whiteCount += 1

    if whiteCount == targetN * targetN:
        whitePaper += 1
        return True

    elif whiteCount == 0:
        bluePaper += 1
        return True

    else:
        return False


def dividConquer(targetN, x, y):
    global whitePaper, bluePaper
    if targetN == 1:
        if coloredPaper[y[0]][x[0]] == 1:
            bluePaper += 1
        elif coloredPaper[y[0]][x[0]] == 0:
            whitePaper += 1
        return True

    
    # [x[0], dividX - 1], [y[0], dividY -1]
    # [dividX, x[1]], [y[0], dividY -1]
    # [x[0], dividX - 1], [dividY, y[1]]
    # [dividX, x[1]], [dividY, y[1]]

    if not chkColoredPaper(targetN, x, y):
        targetN = targetN // 2
        dividX = x[0] + targetN
        dividY = y[0] + targetN

        dividConquer(targetN, [x[0], dividX - 1], [y[0], dividY -1])
        dividConquer(targetN, [dividX, x[1]], [y[0], dividY -1])
        dividConquer(targetN, [x[0], dividX - 1], [dividY, y[1]])
        dividConquer(targetN, [dividX, x[1]], [dividY, y[1]])


dividConquer(n, [0,n-1], [0,n-1])
print(f"{whitePaper}")
print(f"{bluePaper}")