import ctypes

class DynamicArray: 

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self.makeArray(self.capacity)

    def __length__(self):
        return self.size

    def getItem(self, n):
        if not 0 <= n < self.size:
            return IndexError('Index Out of Bounds')

        return self.arr[n]

    def add(self, element):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)

        self.array[self.size] = element
        self.size += 1

    def __resize(self, newCapacity):
        tmpArray = self.makeArray(newCapacity)

        for i in range(self.size):
            tmpArray[i] = self.array[i]

        self.array = tmpArray
        self.capacity = newCapacity

    def makeArray(self, size):
        return (size * ctypes.py_object)()

Array = DynamicArray()
Array.add(1)

print(Array.__length__)
print(Array.capacity)

