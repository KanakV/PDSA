from queue import Queue

def makeAList(vertices, edges):
    AList = {}
    for vertex in vertices:
        AList[vertex] = []

    for (i, j) in edges:
        AList[i].append(j)
        AList[j].append(i)
    
    return AList

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

def findComponents_undirectedGraph(vertices, edges):
    n = len(vertices)
    
    AList = makeAList(vertices, edges)
    
    visitedVertices = {}
    for vertex in vertices:
        visitedVertices[vertex] = False
    
    numVisitedVertices, graphNum = 0, 0
    
    while numVisitedVertices < n:
        startVertex = min(i for i in AList.keys() if not visitedVertices[i])

        connected = BFS(startVertex, AList)
        
        for vertex in connected.keys():
            if connected[vertex]:
                numVisitedVertices += 1
                visitedVertices[vertex] = True

        graphNum += 1
        
    return graphNum