from queue import Queue

def findMasterTank(tanks, pipes):
    Hlist, GList = {}, {}
    for tank in tanks:
        Hlist[tank] = []
        GList[tank] = []
    
    for inlet, outlet in pipes:
        Hlist[outlet].append(inlet)
        GList[inlet].append(outlet)
    
    for tank in tanks:
        if len(Hlist[tank]) == 0 and isConnected(tank, GList):
            return tank
    
    return 0

def BFS(startVertex, AList : dict):
    visitedVertex = {}
    for key in AList.keys():
        visitedVertex[key] = False
    
    processing = Queue()
    processing.put(startVertex)
    visitedVertex[startVertex] = True

    while not processing.empty():
        curr = processing.get()

        for adjVertex in AList[curr]:
            if not visitedVertex[adjVertex]:
                processing.put(adjVertex)
                visitedVertex[adjVertex] = True
    
    return visitedVertex

def isConnected(startVertex, AList):
    visited = BFS(startVertex, AList)

    for vertex in visited.keys():
        if not visited[vertex]:
            return False
    
    return True


v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
    s = input().split(" ")
    e.append((s[0], s[1]))
print(findMasterTank(v, e))