def bubblesort(arr):
    if arr == None or len(arr) < 2:
        return 
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    # arr[i] = arr[i] ^ arr[j]
    # arr[j] = arr[i] ^ arr[j]
    # arr[i] = arr[i] ^ arr[j]

#每次选择最小的排在前面
def selectionsort(arr):
    if arr == None or len(arr) < 2:
        return
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            minIndex = j if arr[j] < arr[minIndex] else minIndex
        swap(arr, i, minIndex)
    return arr

"""插入排序，类似扑克牌牌顺序，
前面的位置都排好序，新数据依次与前面的数比较，交换"""
def insertsort(arr):
    if arr == None or len(arr) < 2:
        return
    for i in range(1,len(arr)):
        j = i-1
        while j >= 0 and arr[j] > arr[j+1]:
            swap(arr, j, j+1)
            j -= 1
    return arr

"""归并排序
将数据分块，分别排序，借助辅助数组，通过外排的方式(两个指针)
将数据放入辅助数组，最后copy到原数组
"""
def mergesort(arr):
    if arr == None or len(arr) < 2:
        return
    sortprocess(arr, 0, len(arr)-1)
    return arr

def sortprocess(arr, l, r):
    if l == r:
        return
    mid = l +((r-l) >> 1)
    sortprocess(arr, l, mid)
    sortprocess(arr, mid+1, r)
    merge(arr, l, mid, r)
#外排序
def merge(arr, l, mid, r):
    helparr = [None] * (r-l+1)
    i = 0
    p1 = l
    p2 = mid+1
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            helparr[i] = arr[p1]
            p1 += 1
            i += 1
        else:
            helparr[i] = arr[p2]
            p2 += 1
            i += 1
    while p1 <= mid:
        helparr[i] = arr[p1]
        p1 += 1
        i += 1
    while p2 <= r:
        helparr[i] = arr[p2]
        p2 += 1
        i += 1
    for j in range(len(helparr)):
        arr[l+j] = helparr[j]