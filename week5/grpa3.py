# Using Belleman-Ford Algorithm
def IsNegativeWeightCyclePresent(WList):
    weights = {}

    inf = max(dist for vertex in WList.keys() for _, dist in WList[vertex])

    for vertex in WList.keys():
        weights[vertex] = inf
    
    weights[0] = 0

    for _ in range(len(WList.keys()) - 1):

        for vertex in WList.keys():
            for adjVertex, weight in WList[vertex]:
                if weights[adjVertex] > weights[vertex] + weight:
                    weights[adjVertex] = weights[vertex] + weight
    
    for vertex in WList.keys():
        for adjVertex, weight in WList[vertex]:
            if weights[adjVertex] > weights[vertex] + weight:
                return True

    return False


# size = int(input())
# edges = eval(input())

size = 4
# edges = [(0,1,10),(0,2,-5),(0,3,2),(3,2,-5),(2,1,-20),(1,3,10)]
edges = [(0,1,10),(0,2,-5),(0,3,2),(3,2,-5),(2,1,-2),(1,3,10)]

WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))