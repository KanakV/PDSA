def MoM7Pos(arr:list):
    median = MoM(arr)

    best = None  # (value, index)

    for i, val in enumerate(arr):
        if val > arr[median]:
            if best is None or val < best[0]:
                best = (val, i)
    
    return best  # returns (value, index) or None

def MoM(arr:list):
    n = len(arr)
    if n <= 5:
        arr.sort()
        
        for median in arr:
            if median[0] == arr[n // 2][0]:
                return median[1]
            
        # for i in range(1, n):
        #     if arr[-i][0] == arr[n//2][0]:
        #         return arr[-i][1] + 1          

    medians = []

    for i in range(0, n, 5):
        temp = []

        for j in range(5):
            temp.append((arr[i + j], i + j))
        
        temp.sort()
        median = temp[3]
        
        for k in range(1, 5, 1):
            if temp[-k][0] == median[0]:
                median = temp[-k]
                break

        medians.append(median)
    
    
    return MoM(medians)




# arr=[int(item) for item in input().split(" ")]
arr = [44, 9, 31, 12, 15, 98, 48, 45, 13, 75, 23, 6, 35, 74]
# arr = [5, 4, 3, 1, 1, 4, 6, 1, 4, 1, 4, 3, 3, 3, 2, 5, 6, 3, 5, 4, 6, 5, 2, 4, 5, 6, 5, 4]

arr = [4, 3, 5, 6, 2, 1, 8, 9, 7, 10, 13, 15, 18, 17, 11, 17, 20, 12, 19, 14, 24, 21, 18, 25, 23]

print(MoM7Pos(arr))
arr.sort()
