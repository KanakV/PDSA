class maxheap:
    def __init__(self):
        self.A = []
    def max_heapify(self,k):
        l = 2 * k + 1
        r = 2 * k + 2
        largest = k
        if l < len(self.A) and self.A[l] > self.A[largest]:
            largest = l
        if r < len(self.A) and self.A[r] > self.A[largest]:
            largest = r
        if largest != k:
            self.A[k], self.A[largest] = self.A[largest], self.A[k]
            self.max_heapify(largest)

    def build_max_heap(self,L):
        self.A = []
        for i in L:
            self.A.append(i)
        n = int((len(self.A)//2)-1)
        for k in range(n, -1, -1):
            self.max_heapify(k)



heap = maxheap()
heap.build_max_heap([66, 55, 43, 34, 12, 7, 2, 20, 5])
print(heap.A)