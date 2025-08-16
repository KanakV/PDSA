from queue import Queue

# Perform Breadth First Search
# Implement a Queue
def findConnectionLevel(n, Gmat, Px, Py):
    # No one is visited so searched = False
    searched = {}
    connectivity = {}

    for i in range(n):
        searched[i] = False
        connectivity[i] = 0
    
    searched[Px] = True
    process = Queue()
    
    process.put(Px)
    
    while not process.empty():
        curr = process.get()
        
        if Gmat[curr][Py] == 1:
            return connectivity[curr] + 1

        for i in range(n):
            if Gmat[curr][i] == 1 and searched[i] == False:
                process.put(i)
                searched[i] = True
                connectivity[i] = connectivity[curr] + 1

        
    return 0

vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))