# Implement merge sort and count

def countintersection(X1:list, X2:list):
    lines = []
    X2c = []
    for i in range(len(X1)):
        lines.append((X1[i], X2[i]))
        X2c.append(X2[i])
    
    X2c.sort()
    lines.sort()

    order = []
    for line in lines:
        order.append(X2c.index(line[1]))

    return sortCount(order)[1]

def sortCount(l):
    n = len(l)
    if n <= 1:
        return l, 0
    
    left, invL = sortCount(l[:n//2])
    right, invR = sortCount(l[n//2:])
    
    arr, invM = mergeCount(left, right)

    return arr, (invL + invR + invM)

def mergeCount(left, right):
    merged = []
    nl = len(left)
    nr = len(right)

    i, j, count = 0, 0, 0
    while i < nl and j < nr:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif right[j] < left[i]:
            merged.append(right[j])
            j += 1
            count += (nl) - i
    
    while i < nl:
        merged.append(left[i])
        i += 1
    
    while j < nr:
        merged.append(right[j])
        j += 1
    
    return merged, count

# L1 = [int(i) for i in input().split(" ")]
# L2 = [int(i) for i in input().split(" ")]
L1 = [8, 22, 10, 4, 17, 14]
L2 = [15, 18, 3, 12, 10, 23]
L1 = [0, 1, 2, 3, 4]
L2 = [0, 1, 2, 3, 4]
L1 = [0, 1]
L2 = [1, 0]

print(countintersection(L1, L2))
timeout = 2.0  # Timeout in sec
