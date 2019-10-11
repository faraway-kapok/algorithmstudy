"""
运用归并，求取逆序对
"""
def inversepair(arr):
    if arr == None or len(arr) < 2:
        # return []
        return 0
    return mergesort(arr, 0, len(arr)-1), arr

def mergesort(arr, l, r):
    if l == r:
        # return []
        return 0

    mid = l + ((r-l) >> 1)

    return mergesort(arr, l, mid) + mergesort(arr, mid+1, r) +\
           merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    temp = []
    p1 = l
    p2 = mid + 1
    # res = []
    res = 0
    while p1 <= mid and p2 <= r:
        if arr[p1] > arr[p2]:
            # for j in range(p1, mid+1):
            #     res.append((arr[j], arr[p2]))
            res += mid-p1+1
            temp.append(arr[p2])
            p2 += 1
        else:
            temp.append(arr[p1])
            p1 += 1
    while p1 <= mid:
        temp.append(arr[p1])
        p1 += 1
    while p2 <= r:
        temp.append(arr[p2])
        p2 += 1
    # print(temp)
    for i in range(len(temp)):
        arr[l+i] = temp[i]
    return res

if __name__ == "__main__":
    arr = [7,5,6,4]
    res = inversepair(arr)
    print(res)
    