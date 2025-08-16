def findLeft(arr, x, start, end):
    mid = start + (end - start) // 2
    if end <= start:
        return mid
    if mid - 1 < start and arr[mid] == x:
        return mid
    
    if arr[mid - 1] != x and arr[mid] == x:
        return mid
    elif arr[mid - 1] and arr[mid] == x:
        return findLeft(arr, x, start, mid - 1)
    else:
        return findLeft(arr, x, mid + 1, end)

def findRight(arr, x, start, end):
    mid = (start + end) // 2
    if end <= start:
        return mid
    if mid + 1 > end:
        return mid
    
    if arr[mid + 1] != x and arr[mid] == x:
        return mid
    elif arr[mid + 1] and arr[mid] == x:
        return findRight(arr, x, mid + 1, end)
    else:
        return findRight(arr, x, start, mid - 1)

def searchPos(arr, x, start, end):
    mid = (start + end) // 2

    if end <= start and arr[mid] != x:
        return None, None
    

    if arr[mid] == x:
        left = findLeft(arr, x, start, mid)
        right = findRight(arr, x, mid, end)
        return left, right
    if arr[mid] < x:
        return searchPos(arr, x, mid + 1, end)
    elif arr[mid] > x:
        return searchPos(arr, x, start, mid)
    
    return
 
def findOccOf(L, x):
    return searchPos(L, x, 0, len(L) - 1)

A = [int(item) for item in input().split(" ")]
x = int(input())
timeout = 1.0 # Timeout in sec

# A = [3, 3, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 10, 10, 11, 13, 14, 14, 14, 14, 14, 14]
# A = [3, 3, 3, 3, 3]
# A = [1, 2, 3, 4]
# x = 3
# print(findOccOf(A, x))
