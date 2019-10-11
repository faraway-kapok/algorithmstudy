"""题目：
一根金条长为60，切成10,20,30的三部分，问怎样切花费最少
其中，金条有多长就花费多少铜板，假设金条为60，则，不管金条
切成多少比例的两块，总花费都是60铜板
要求：
如果arr长度为N，时间复杂度为O(NlogN)

思路：
将待切部分构成小根堆，依次从小根堆里取出最小的两个数
求和，再放进小根堆里，循环往复，直到小根堆的大小为1
即构成哈夫曼树。
所有非叶子结点加起来即为最后的结果

一共N个数，总的合并次数为O(N),每次合并需要小根堆
的压入和弹出炒作O(logN),所有全部过程为O(NlogN)
"""

import heapq
def getMinSplitCost(arr):
    if arr == None or len(arr) < 2:
        return 0
    
    heapq.heapify(arr)

    ans = 0
    while len(arr) != 1:
        sum_ = heapq.heappop(arr) + heapq.heappop(arr)
        ans += sum_
        heapq.heappush(arr, sum_)
        # print(heap.getheapSize())
    return ans

import queue
"""尚未跑通"""
def cut_gold_bar(arr):
    arr_list = []
    prio_queue = queue.PriorityQueue()
    for item in arr:
        prio_queue.put(item)
    while not prio_queue.empty():
        if prio_queue.qsize == 1:
            prio_queue.get()
        else:
            item_sum = prio_queue.get() + prio_queue.get()
            arr_list.append(item_sum)
            prio_queue.put(item_sum)
    return arr_list


if __name__ == "__main__":
    arr = [3,9,5,2,4,4]
    print(getMinSplitCost(arr))
    # print(cut_gold_bar(arr))
