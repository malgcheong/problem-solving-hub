n = int(input())
values = list(map(int, input().split()))

m = int(input())
selects = list(map(int, input().split()))

values.sort()

def binarySearch(pl, pr):
    pc = ((pr - pl + 1) // 2 ) + pl
    if pl > pr:
        return print(0)
    
    elif values[pc] == select:
        return print(1)

    elif values[pc] > select:
        return binarySearch(pl,pc-1)
        
    elif values[pc] < select:
        return binarySearch(pc+1, pr)

for select in selects:
    binarySearch(0, len(values)-1)
    