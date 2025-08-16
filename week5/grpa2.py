# Using dijkstras Algorithm

def dijkstra(WList, src, dst):
    distFrmSrc, visited, previous = {}, {}, {}

    inf = len(WList.keys()) * max(dist for vertex in WList.keys() for _, dist in WList[vertex])

    for vertex in WList.keys():
        distFrmSrc[vertex], visited[vertex] = inf, False

    distFrmSrc[src] = 0
    previous[src] = None
    curr = src

    while not visited[dst]:
        visited[curr] = True

        for adjVertex, dist in WList[curr]:
            if not visited[adjVertex]:
                distFrmSrc[adjVertex] = min(distFrmSrc[curr] + dist, distFrmSrc[adjVertex])
                if distFrmSrc[adjVertex] ==  distFrmSrc[curr] + dist:
                    previous[adjVertex] = curr

        minDistFrmSrc = inf
        closest = None
        for vertex in WList.keys():
            if not visited[vertex] and distFrmSrc[vertex] < minDistFrmSrc:
                minDistFrmSrc = distFrmSrc[vertex]
                closest = vertex
        
        curr = closest

    return distFrmSrc, previous

def findPath(prev, dst):
    path = []

    curr = dst
    while not curr == None:
        path.append(curr)
        curr = prev[curr] 

    path.reverse()
    return path

# def findPath(WList, dist, src, dst):
#     path = [dst]
#     inf = dist[dst]
#     curr = dst

#     while curr != src:
#         minDist = inf
#         nextVertex = None

#         for adjVertex, _ in WList[curr]:
#             if dist[adjVertex] < minDist:
#                 nextVertex = adjVertex
#                 minDist = dist[adjVertex]
        
#         path.append(nextVertex)
#         curr = nextVertex

#     path.reverse()
#     return path


def min_cost_walk(WList, src, dst, via):
    
    # Initialisation
    graphDist = 0

    dist, links = dijkstra(WList, src, via)
    
    graphDist += dist[via]
    path = findPath(links, via)

    dist, links = dijkstra(WList, via, dst)
    graphDist += dist[dst]
    nextpath = findPath(links, dst)
    
    for vertex in nextpath[1:]:
        path.append(vertex)

    return graphDist, path



# size = int(input())
# edges = eval(input())
# S= int(input())
# D=int(input())
# V=int(input())

# size = 7
# edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
# S = 0
# D = 4
# V = 5

size = 7
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
S = 0
D = 4
V = 3

WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))