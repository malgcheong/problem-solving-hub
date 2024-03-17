import sys
list = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

def mergeSort(list):
    # split 완료
    if len(list) == 1:
        return list
    
    left = list[0:len(list)//2]
    right = list[len(list)//2:]

    # split 코드
    left = mergeSort(left)
    right = mergeSort(right)

    # merge 코드
    list = []
    while left:
        if not right:
            list.extend(left)
            left = []
            continue
        if left[0] > right[0]:
            list.append(right[0])
            del right[0]
        else:
            list.append(left[0])
            del left[0]
    list.extend(right)

    return list

list = mergeSort(list)
[print(li) for li in list]