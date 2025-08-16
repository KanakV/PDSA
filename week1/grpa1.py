def find_Min_Difference(L : list, P : int):
    
    L.sort()
    min = L[-1]
    
    for i in range(len(L) - P + 1):
        if L[i + P - 1] - L[i] < min:
            min = L[i + P - 1] - L[i]

    return min

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))