'''
implement the function closest_pair_min_difference(L) takes list L and return smallest absolute 
difference between pairs of elements - the worst case is O(n.log(n)) 
ex:- L = [5,2,3,4,1] 
here several pairs have min difference of 1 : 
[(1,2),(2,3),(3,4),(4,5)] return smallest absolute difference value between pairs of 
elements : 1 
[5,4,3,2] ---> 1 
[1,1,4,6,8] ---> 0
'''

# Implement a sorting algo
def closest_pair_min_difference(L):
    L_sorted = merge_sort(L)
    
    #print(L_sorted)

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
    #print(left)
    right = SortInPlace(L, mid + 1, n - 1)
    #print(right)
    sorted = merge(left, right)

    return sorted

def SortInPlace(L, start, end):
    if end <= start:
        return [L[start]]
    
    mid = (start + end) // 2
    left = SortInPlace(L, start, mid)
    #print(left)
    right = SortInPlace(L, mid+1, end)
    #print(right)
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
