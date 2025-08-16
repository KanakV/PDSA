class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, index):
        left    = 2 * index + 1
        right   = 2 * index + 2

        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)
    
    def buildHeap(self, list):
        # O(n)
        self.heap = list

        n = int(len(self.heap) // 2 - 1)

        for i in range(n, -1, -1):
            self.heapify(i)    

def min_max(arr : list):
    maxHeap = MaxHeap()
    maxHeap.buildHeap(arr)

    return maxHeap.heap



# arr = input("List: ")
arr = "66 55 43 34 12 7 2 20 5"
# arr = "10 14 19 26 31 42 27 44 35 33"
arr = arr.split(" ")
for element in arr:
    element = int(element)

print(arr)
print(min_max(arr))