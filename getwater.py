"""容器盛水问题"""
def getwater1(arr):
    if arr == None or len(arr) < 3:
        return 0
    leftmaxs = [0] * len(arr)
    rightmaxs = [0] * len(arr)
    leftmaxs[0] = arr[0]
    rightmaxs[-1] = arr[-1]
    for i in range(1,len(arr)):
        leftmaxs[i] = max(leftmaxs[i-1], arr[i])
    for i in range(len(arr)-2,-1,-1):
        rightmaxs[i] = max(rightmaxs[i+1], arr[i])
    res = 0
    for i in range(1,len(arr)-1):
        res += max(min(leftmaxs[i-1],rightmaxs[i+1])-arr[i], 0)
    return res
def getwater(arr):
    if arr == None or len(arr) < 3:
        return 0
    res = 0
    leftmax = arr[0]
    rightmax = arr[-1]
    l = 1
    r = len(arr) - 2
    while l <= r:
        if leftmax <= rightmax:
            res += max(0, leftmax-arr[l])
            leftmax = max(leftmax, arr[l])
            l += 1
        else:
            res += max(0, rightmax-arr[r])
            rightmax = max(rightmax, arr[r])
            r -= 1
    return res

if __name__ == "__main__":
    arr = [3,1,2,5,2,4]
    arr1 = [4,5,1,3,2]
    print(getwater1(arr))
    print(getwater1(arr1))
    print(getwater(arr))
    print(getwater(arr1))



    