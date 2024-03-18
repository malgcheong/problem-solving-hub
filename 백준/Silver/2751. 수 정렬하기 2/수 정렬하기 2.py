
# 합병 정렬
import sys
list = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

def sort(list):
    if len(list) < 2:
        return list
    left = sort(list[:len(list)//2])
    right = sort(list[len(list)//2:])
    return mergeSort(left, right)

def mergeSort(left, right):

    new_list=[]
    i=0
    j=0

    while (i<len(left)) & (j<len(right)):
        if left[i]>right[j]:
            new_list.append(right[j])
            j+=1
        else:
            new_list.append(left[i])
            i+=1
    while (j<len(right)):
            new_list.append(right[j])
            j+=1
    while (i<len(left)):
            new_list.append(left[i])
            i+=1
    return new_list



[print(li) for li in sort(list)]