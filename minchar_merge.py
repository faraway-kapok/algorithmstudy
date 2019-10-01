"""
字典序
# 实现几个字符串的拼接，使得他们的值最低。
# 字符串的值是这样定义的： 字符串的ascii代表它的值，字符串的位置代表的百分位
# 比如 'ab'  ord('a') = 97 ord('b') = 98  'ab'的值为97*10+98=1068 
#  'ba'的值为98*10+97=1077 ，'ba'>'ab'

"""
def min_merge(arr):
    if not arr:
        return []
    min_str_arr = [arr[0]]
    for i in range(1,len(arr)):
        j = len(min_str_arr) - 1
        while j >= 0:
            if min_str_arr[j] + arr[i] > arr[i] + min_str_arr[j]:
                j -= 1
            else:
                break
        min_str_arr.insert(j+1, arr[i])
    return min_str_arr

if __name__ == "__main__":
    strs1 = ['jibw', 'ji', 'jp', 'bw', 'jibw']
    print(min_merge(strs1))
    strs2 = ['ba', 'b']
    print(min_merge(strs2))