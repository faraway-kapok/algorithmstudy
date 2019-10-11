"""
运用归并
小和运算，求一个数之前小于它的数字之和"""
def smallSum(arr):
    if arr == None or len(arr) < 2:
        return 0
    return mergeSort(arr, 0, len(arr)-1)
#返回在l与r之间产生多少小和
def mergeSort(arr, l, r):
    if l == r:
        return 0
    mid = l + ((r-l)>>1)
    return mergeSort(arr, l, mid) + mergeSort(arr, mid+1, r) \
           + merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    temp = []
    p1 = l
    p2 = mid + 1
    res = 0
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            res += (r-p2+1) * arr[p1]
            temp.append(arr[p1])
            p1 += 1
        else:
            res += 0
            temp.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        temp.extend(arr[p1:mid+1])
    while p2 <= r:
        temp.extend(arr[p2:+ r+1])
    for i in range(len(temp)):
        arr[l+i] = temp[i]

    return res