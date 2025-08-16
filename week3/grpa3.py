def reverse(root):
    
    prevNode = None
    currNode = root
    nextNode = currNode.next
    
    while nextNode is not None:
        currNode.next = prevNode
        
        prevNode = currNode
        currNode = nextNode
        nextNode = nextNode.next
    
    currNode.next = prevNode
    return currNode