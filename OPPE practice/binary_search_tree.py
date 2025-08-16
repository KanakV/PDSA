class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
def insert_element(root,k):

    curr = root
    prev = curr
    while curr is not None:
        prev = curr
        if k < curr.data:
            curr = curr.left
        elif k > curr.data:
            curr = curr.right
    if k < prev.data:
        prev.left = Node(k)
    elif k > prev.data:
        prev.right = Node(k)
