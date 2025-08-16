class Tree:
  #constructor
    def __init__(self, initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = self.right = None
        return
    
    #Only empty node has value None
    def isempty(self):
        return(self.value == None)
    
    #Leaf nodes have both children empty
    def isleaf(self):
        return(self.value != None and self.left.isempty() and self.right.isempty())
  
#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
    temp = root
    while (not temp.isempty()):
        if (x < temp.value):
            temp = temp.left
        else:
            temp = temp.right

    temp.value = x
    temp.left = Tree()
    temp.right = Tree()

def maxLessThan(root, x):
    curr = root
    while not curr.isempty():
        
        if curr.value > x:
            if curr.left.isempty():
                return None
            curr = curr.left
        elif curr.value < x:
            if curr.right.isempty() or curr.right.value > x :
                return curr.value
            curr = curr.right

    return None

# L = [int(item) for item in input().split(" ")]
# x = int(input())

# L = [50, 52, 54, 74, 93, 100, 114, 124, 130, 143]
# x = 145
# L = [23235, 82107, 35775, 91961, 4323, 40556, 76603, 64302, 27316, 74372]
# x = 2000
# L = [20, 10, 30]
# x = 19

L = [50, 36, 28, 40, 19, 21]
x = 35


root = Tree(L[0])
for item in L[1:]:
    insertToBST(root, item)

print(maxLessThan(root, x))