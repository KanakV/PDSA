# Using Prims Algorithm
def FiberLink(WList : dict):
    weights, visited = {}, {}
    graphWeight = 0
    
    inf = len(WList.keys()) * max(dist for vertex in WList.keys() for _, dist in WList[vertex])

    for vertex in WList.keys():
        weights[vertex], visited[vertex] = inf, False
    
    weights[0] = 0
    visited[0] = True

    for _ in range(len(WList.keys()) - 1):
        mindist = inf
        nextVertex = None

        for vertex in WList.keys():
            for adjVertex, dist in WList[vertex]:
                if visited[vertex] and not visited[adjVertex] and dist < mindist:
                    mindist = dist
                    nextVertex = adjVertex
        
        graphWeight += mindist
        visited[nextVertex] = True


    return graphWeight


# size = int(input())
# edges = eval(input())

size = 7
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))