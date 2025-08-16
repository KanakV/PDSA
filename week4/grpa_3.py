from queue import Queue

def longJourney(AList):
    # Perform topological sort + longest path calculation
    vertices = AList.keys()

    indegree, longest_path = {}, {}
    
    iAList = invAList(AList)
    
    # Initialising the Indegree & Longest Path dictionaries
    for vertex in vertices:
        indegree[vertex] = len(iAList[vertex])
        longest_path[vertex] = 0
        
    # Adding all 0 degree vertices to the queue
    zeroDegreeVertex = Queue()
    
    for vertex in vertices:
        if indegree[vertex] == 0:
            zeroDegreeVertex.put(vertex)

    while not zeroDegreeVertex.empty():
        curr = zeroDegreeVertex.get()

        indegree[curr] -= 1

        for adjVertex in AList[curr]:
            indegree[adjVertex] -= 1
            longest_path[adjVertex] = max(longest_path[curr], longest_path[adjVertex]) + 1
            
            if indegree[adjVertex] == 0:
                zeroDegreeVertex.put(adjVertex)

    # Back track from longest path
    lpath = max(longest_path[city] for city in vertices)
    path = []

    for vertex in vertices:
        if longest_path[vertex] == lpath:
            path.append(vertex)
            break

    for i in range(lpath):
        curr = path[i]
        pathLen = lpath - i - 1 

        for adjVertex in iAList[curr]:
            if longest_path[adjVertex] == pathLen:
                path.append(adjVertex)
                break
    path.reverse()
    return path

def invAList(AList):
    
    iAList = {}
    
    for vertex in AList.keys():
        iAList[vertex] = []
    
    for vertex in AList.keys():
        for adjVertex in AList[vertex]:
            iAList[adjVertex].append(vertex)
    
    return iAList


AList = {'Madurai': ['Cochin', 'Kanyakumari'],
 'Vaishali': [],
 'Varanasi': ['Khajuraho', 'Bodhgaya'],
 'Thiruvanandhapuram': ['Kanyakumari'],
 'Udaipur': ['Gir', 'Ajanta'],
 'Rishikesh': ['Delhi'],
 'Shimla': ['Rishikesh'],
 'Bangalore': ['Chennai', 'Madurai'],
 'Agra': ['Ranthambore'],
 'Ellora': ['Aurangabad'],
 'Bodhgaya': ['Kolkatta'],
 'Cochin': ['Thiruvanandhapuram'],
 'Pushkar': ['Udaipur', 'Ranthambore'],
 'Ranthambore': ['Khajuraho'],
 'Gir': [],
 'Aurangabad': ['Mumbai'],
 'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
 'Chennai': ['Madurai'],
 'Sravasti': ['Kushinagar'],
 'Leh': ['Shimla'],
 'Sarnath': ['Varanasi'],
 'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
 'Goa': ['Cochin', 'Bangalore'],
 'Kanyakumari': [],
 'Kushinagar': ['Sarnath', 'Vaishali'],
 'Khajuraho': ['Ajanta'],
 'Jaipur': ['Pushkar'],
 'Mumbai': ['Goa'],
 'Ajanta': ['Ellora', 'Aurangabad']
 }
 
 

print(longJourney(AList))