# 4시 30분
import sys
n = int(sys.stdin.readline())

pole = [int(sys.stdin.readline()) for _ in range(n)]

rightPole = pole[-1]

# rightPole 얘보다 높은 것만 보인다.
# pop 하면서 얘보다 높은 것만 cnt로 저장

# 첫번째 놈은 일단 보이니깐 바로 pop
cnt = 1
pole.pop()
while len(pole) != 0:
    if pole[-1] > rightPole:
        rightPole = pole[-1]
        cnt += 1
    pole.pop()

print(cnt)

