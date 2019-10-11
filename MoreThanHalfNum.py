
"""数组中出现次数超过一半的数字"""
import random
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0

        length  = len(numbers)
        mid = length >> 1
        l = 0
        r = length -1
        arr = numbers
        self.swap(numbers, l + random.randint(0, r-l+1), r)
        left, right = self.partition(arr, l, r)
        while mid not in range(left, right+1):           
            if mid < left:
                left, right = self.partition(arr, l, left-1)
            elif mid > right:
                left, right = self.partition(arr, right+1, r)
        times = right - left + 1
        if times > mid:
            return arr[left]
        else:
            return 0   
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def partition(self, arr, l, r):
        less = l - 1
        more = r
        while l < more:
            if arr[l] < arr[r]:
                less += 1
                self.swap(arr, l, less)
                l += 1
            elif arr[l] > arr[r]:
                more -= 1
                self.swap(arr, l, more)
            else: 
                l += 1
        self.swap(arr, more, r)
        return less+1, more-1

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        time = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                time += 1
        if time*2 <= len(numbers):
            return 0
        else:
            return result
        