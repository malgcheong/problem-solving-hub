width, height = map(int, input().split())

listX, listY = [0, width], [0, height]
for _ in range(int(input())):

    xy, point = map(int, input().split())
    
    if xy == 0:
        listY.append(point)
    elif xy == 1:
        listX.append(point)

listX.sort(), listY.sort() 

maxX = max([listX[i+1] - listX[i] for i in range(len(listX)-1)])
maxY = max([listY[i+1] - listY[i] for i in range(len(listY)-1)])
print(maxX * maxY)
