def mergeSort(arr):
    if arr == None or len(arr) < 2:
        return
    sortProcess(arr,0, len(arr)-1)

def sortProcess(arr, L, R):
    if L == R:
        return
    mid = L + ((R-L)>>1)
    sortProcess(arr, L, mid)
    sortProcess(arr, mid+1, R)
    Merge(arr, L, mid, R)

def Merge(arr, L, mid, R):
    temp = []
    p1 = L
    p2 = mid + 1
    while(p1 <= mid and p2 <= R):
        if arr[p1] < arr[p2]:
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1
    
    while(p1 <= mid):
        temp.extend(arr[p1:mid+1])
    while(p2 <= R):
        temp.extend(arr[p2:R+1])
        p2 += 1
    for i in range(len(temp)):
        arr[L+i] = temp[i]
