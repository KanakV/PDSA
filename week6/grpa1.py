class minHeap():
    def __init__(self):
        # Heap will contain list of tuples corresponding to (value, list ID)
        self.heap = []

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        return False

    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1
        
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent][0] > self.heap[index][0]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def get_min(self):
        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0] 
        v = self.heap.pop()

        parent = 0
        while True:
            left    = 2 * parent + 1
            right   = 2 * parent + 2 
            
            minIndex = parent

            if left < len(self.heap) and self.heap[left][0] < self.heap[minIndex][0]:
                minIndex = left
            if right < len(self.heap) and self.heap[right][0] < self.heap[minIndex][0]:
                minIndex = right
            if minIndex != parent:
                self.heap[parent], self.heap[minIndex] = self.heap[minIndex], self.heap[parent]
                parent = minIndex
            else:
                break

        return v


# O(n log k)
def mergeKLists(LL):
    sortedList = []

    front = minHeap()

    # O(log k!)
    for i, L in enumerate(LL):
        front.insert((L[0], i))
    
    # O(k)
    listPointer = [1 for _ in LL]

    # O(n)
    while not front.isEmpty():
        # O(log k)
        value, listNum = front.get_min()
        sortedList.append(value)

        # figure out a way to go through each sublist
        if listPointer[listNum] < len(LL[listNum]):
            # O(log k)
            front.insert((LL[listNum][listPointer[listNum]], listNum))
            listPointer[listNum] += 1



    return sortedList


# k = int(input())
# LL=[]
# for i in range(k):
#     subL = [int(item) for item in input().split(" ")]
#     LL.append(subL)


# LL = [  [4, 5],
#         [8, 26, 69]
#     ]

LL = [[4, 5, 13, 17],
[8, 26, 69, 122, 135],
[10, 101, 125, 450]
]
print(mergeKLists(LL))