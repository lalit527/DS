import ctypes
class BinaryHeap:
    def __init__(self, capacity = 16):
        self.heap = self.makeArray(capacity)
        self.capacity = capacity
    
    def addHeap(self, arr):
        for i in range(len(arr)):
            self.heap[i] = arr[i]
        self.capacity = len(arr)

    def parent(self, i):
        return i//2

    def left(self, i):
        return (2 * i) + 1

    def right(self, i):
        return (2 * i) + 2

    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < len(self.heap) and ( self.heap[l] > self.heap[i] ):
            largest = l 
        
        if r < len(self.heap) and ( self.heap[r] > self.heap[largest] ):
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        length = len(self.heap) - 1
        for i in range(length//2, -1, -1):
            print(i)
            self.maxHeapify(i)

    def insert(self, n):
        length = len(self.heap)
        if len(self.heap) == self.capacity:
            self.increaseHeapCapacity(2 * self.capacity)
        tmp = self.heap[0]
        self.heap[0] = n
        self.heap[length] = tmp
        self.maxHeapify(0)

    def increaseHeapCapacity(self, newCapacity):
        tmpArray = self.makeArray(newCapacity)

        for i in range(len(self.heap)):
            tmpArray[i] = self.heap[i]

        self.heap = tmpArray
        self.capacity = newCapacity


    def makeArray(self, size):
        return (size * ctypes.py_object)

        

arr = [ 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = BinaryHeap()
heap.addHeap(arr)
print(heap.heap)
heap.buildMaxHeap()
heap.insert(12)
print(heap.heap)