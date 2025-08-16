# Implement a sorting algo
def closest_pair_min_difference(L):
    L_sorted = merge_sort(L)
    min_diff = L_sorted[-1] - L_sorted[0]
    
    for i in range(len(L_sorted) - 1):
        diff = L_sorted[i+1] - L_sorted[i] 
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

def merge_sort(L):
    n = len(L)
    mid = n // 2

    left = SortInPlace(L, 0, mid)
    right = SortInPlace(L, mid + 1, n - 1)
    sorted = merge(left, right)

    return sorted

def SortInPlace(L, start, end):
    if end <= start:
        return [L[start]]
    
    mid = (start + end) // 2
    left = SortInPlace(L, start, mid)
    right = SortInPlace(L, mid+1, end)
    L_sort = merge(left, right)

    return L_sort

def merge(left, right):
    L_sort = []
    i, j = 0, 0
    l, r = len(left), len(right)

    while i < l and j < r:
        if left[i] < right[j]:
            L_sort.append(left[i])
            i += 1
        else:
            L_sort.append(right[j])
            j += 1

    while i < l:
        L_sort.append(left[i])
        i += 1
    
    while j < r:
        L_sort.append(right[j])
        j += 1
    
    return L_sort


    
L = [1,1,4,6,8]
print(closest_pair_min_difference(L))
