"""荷兰国旗，<x , x, >x """
def partition(arr, l, r, num):
    less = l - 1
    more = r + 1
    
    #l指向当前指针
    while l < more:
        if arr[l] < num:
            less += 1
            swap(arr,less, l)
            l += 1
        elif arr[l] > num:
            more -= 1
            # print(more)
            swap(arr, more, l)
        else:
            l += 1
    return less+1, more-1 #返回等于num的第一个index以及最后一个index

def swap(arr, i, j):
     tmp = arr[i]
     arr[i] = arr[j]
     arr[j] = tmp 
    
arr = [10,3,4,3,2,1,3,7,5,1]
print(partition(arr, 0, len(arr)-1, 3))
print(arr)