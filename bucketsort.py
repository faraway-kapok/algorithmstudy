"""
求数组排序后，两个相邻数之间最大的差值
借用了桶排序
题目：
给定一个数组，求如果排序后，相邻两数的最大差值，要求时间复杂度O(N),且要求不能用非基于比较的排序
"""
def maxGap(nums):
    if nums == None or len(nums) < 2:
        return 0
    
    length = len(nums)
    minvalue = min(nums)
    maxvalue = max(nums)
    
    if maxvalue == minvalue:
        return 0
    hasNum = [False] * (length+1)
    maxs = [0] * (length+1)
    mins = [0] * (length+1)
    bid = 0
    for i in range(length):
        bid = bucket(nums[i], length, minvalue, maxvalue)
        mins[bid] = mins[bid] if hasNum[bid] and mins[bid] < nums[i] else nums[i]
        maxs[bid] = maxs[bid] if hasNum[bid] and maxs[bid] > nums[i] else nums[i]
        hasNum[bid] = True
    res = 0
    lastMax = maxs[0]
    for i in range(1,length+1):
        if hasNum[i]:
            res = mins[i] - lastMax if res < (mins[i]-lastMax) else res
            lastMax = maxs[i]
    return res

#确定当前数属于几号桶
def bucket(num, length, minvalue, maxvalue):
    return int((num-minvalue)*length/(maxvalue-minvalue))