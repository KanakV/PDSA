# Implement merge sort and count

def countintersection(l1:list, l2:list):
    rl2 = {}

    for i, num in enumerate(l2):
        rl2[num] = i
    
    print(rl2)
    l2.sort()
    
    for i, num in enumerate(l2):
        l2[i] = rl2[num]
    
    mergeSortnCount(l2)
    
    print(l2)

    ...    

def mergeSortnCount(l):
    ...

# L1 = [int(i) for i in input().split(" ")]
# L2 = [int(i) for i in input().split(" ")]
L1 = [8, 22, 10, 4, 17, 14]
L2 = [15, 18, 3, 12, 10, 23]

countintersection(L1, L2)
timeout = 2.0  # Timeout in sec
