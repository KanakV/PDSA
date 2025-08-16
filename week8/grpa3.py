import math

def minDistRec(Px, Py):
    n = len(Px)
    if n == 2:
        return distance(Px[0], Px[1])
    if n == 3:
        return min(distance(Px[0], Px[1]), distance(Px[1], Px[2]), distance(Px[2], Px[0]))
    
    half = n // 2

    # O(n)
    Lx, Rx = Px[:n//2], Px[n//2:]
    # O(nlogn)
    Ly, Ry = sortTuples(Lx, 1), sortTuples(Rx, 1)

    dL = minDistRec(Lx, Ly)
    dR = minDistRec(Rx, Ry)

    mindist = min(dL, dR)
    
    # O(n)
    strip = makeStrip(Px, Py, mindist)

    # O(n)
    mindist = mergeBoundary(strip, mindist)

    return mindist

def mergeBoundary(strip, mindist):
    n = len(strip)
    if n == 1:
        return mindist
    
    strip = sortTuples(strip, 1)

    for i in range(0, n - 1):
        for j in range(i + 1, min(i + 15, n - 1)):
            mindist = min(mindist, distance(strip[i], strip[j]))

    return mindist

def makeStrip(Px, Py, mindist):
    mid = len(Px) // 2

    strip = []
    for point in Px:
        if abs(Px[mid][0] - point[0]) < mindist:
            strip.append(point)
    
    return strip
    
def minDistance(points):
    Px = sortTuples(points, 0)
    Py = sortTuples(points, 1)

    return minDistRec(Px, Py)
    
def sortTuples(tuples:list, index:int):
    key = lambda tuples:int(tuples[index])
    ordered = sorted(tuples, key = key)

    return ordered


def distance(p1, p2):
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


# pts = eval(input())
pts = [(2, 15), (40, 5), (20, 1), (21, 14), (1,4), (3, 11)]
print(minDistance(pts))
timeout = 2.0  # Timeout in sec