import sys
testcase = int(sys.stdin.readline())

for _ in range(testcase):

    n = int(sys.stdin.readline())

    employList = []
    result = []
    for i in range(n):
        drank, irank = map(int, sys.stdin.readline().split())
        employList.append((drank,irank))

    employList.sort(key = lambda x: x[0])
    result.append((employList[0][0], employList[0][1]))

    temp = result[0]
    for dr, ir in employList:
        if temp[1] > ir:
            result.append((dr, ir))
            temp = (dr, ir)            

    print(len(result))