#Vertices are expected to be labelled as single letter or single digit 
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, obj):
        self.stack.append(obj)
    
    def isEmpty(self):
        return self.stack == []
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    
    def __str__(self):
        return str(self.stack)
def DFS():
    ...
    
def findAllPaths(vertices, AList : dict, source, destination):
    visited = {}
    for vertex in vertices:
        visited[vertex] = False

    processing = Stack()
    processing.push(source)

    while not processing.isEmpty():
        curr =  processing.pop()

        if not visited[curr]:
            visited[curr] = True



#Sort and arrange the result for uniformity
def ArrangeResult(result):
    res = []
    for item in result:
        s = ""
        for i in item:
            s += str(i)    
        res.append(s)
    res.sort() 
    return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
    Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))