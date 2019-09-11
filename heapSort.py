def heapSort(arr):
    if arr == None or len(arr) < 2:
        return
    for i in range(len(arr)):
        #建立大根堆
        heapInsert(arr,i) 
    heapSize = len(arr)
    swap(arr, 0, heapSize)
    while heapSize > 0:
        heapify()



#上浮，建立大根堆的过程
def heapInsert(arr, index):
    while arr[index] > arr[(index-1)/2]:
        swap(arr, index, (index-1)/2)
        index = (index-1)/2


def swap(arr, i, j):
     tmp = arr[i]
     arr[i] = arr[j]
     arr[j] = tmp  

#0-heapsize之间形成的堆，若index位置的值变小，下沉
def heapisize(arr, index, heapSize):
    left = index*2 + 1
    largest = 0
    while left < heapSize:
        if left+1 < heapSize and arr[left+1] > arr[left]:
            largest = left + 1
        else:
            largest = left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, index, largest)
        index = largest
        left = index * 2 + 1