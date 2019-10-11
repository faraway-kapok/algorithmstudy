"""n个人报数，每到报到m该人出列，下一个人继续报数，求取胜利者"""
def lastRemaining(n, m):
    if n == 0 or m == 0:
        return -1
    arr = []
    for i in range(n):
        arr.append(i)
    index = 0
    while len(arr) > 1:
        index = (index + m-1) % len(arr)
        arr.pop(index)
    return arr[0] if len(arr) == 1 else -1

if __name__ == "__main__":
    n = 10
    m = 3
    print(lastRemaining(n, m))