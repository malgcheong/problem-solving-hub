import sys

n = int(sys.stdin.readline())

meeting = []
for i in range(n):
    v, u = map(int, sys.stdin.readline().split())
    meeting.append((v,u))

meeting.sort(key=lambda x: (x[1],x[0]))


result = []

result = [meeting[0]]
tempMeeting = meeting[0]
for j in range(1, len(meeting)):
    if tempMeeting[1] <= meeting[j][0]:
        result.append(meeting[j])
        tempMeeting = meeting[j]

print(len(result))
