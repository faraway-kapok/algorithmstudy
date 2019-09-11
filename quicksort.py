"""根据荷兰旗改变后的快排，每次以最后一个数为比较点"""
"""经典快排"""
import random
def quickSort(arr, L, R):
    if L < R:
        #可以添加一个random实现随机快排
        swap(arr,L + random.randint(0,R-L+1), R)
        left, right = partition(arr, L, R)
        quickSort(arr, L, left-1)
        quickSort(arr, right+1, R)


def partition(arr, L, R):
    less = L - 1
    more = R
    while L < more:
        if arr[L] < arr[R]:
            less += 1
            swap(arr, less, L)
            L += 1
        elif arr[L] > arr[R]:
            more -= 1
            swap(arr, L, more)
        else:
            L += 1
    swap(arr, more, R)
    return less+1, more-1

def swap(arr, i, j):
     tmp = arr[i]
     arr[i] = arr[j]
     arr[j] = tmp 


arr = [10,3,4,3,2,1,3,7,5,1]
print(quickSort(arr, 0, len(arr)-1))
print(arr)