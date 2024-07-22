h, m = map(int, input().split())
c = int(input())

count = int((c + m) / 60)
answer_m = (c + m) % 60
answer_h = (h + count) % 24

print(answer_h, answer_m)