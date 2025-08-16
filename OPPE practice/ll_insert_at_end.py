class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next pointer to None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None
    
    def insert_at_end(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return
        
        curr = self.head

        while curr.next is not None:
            curr = curr.next
        
        curr.next = temp
        
# Testing
t = LinkedList()
for el in [1,3,5,7,9]:
    t.insert_at_end(el)

temp = t.head

while temp.next is not None:
    print(temp.data)