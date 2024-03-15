n = int(input())

list = []
for i in range(n):
    list.append(str(input()))

for i in list:
    score = 0
    plus = 0
    for j in i:
        if j == 'O':
            plus += 1
        elif j == 'X':
            plus = 0
        score += plus
    print(score)
