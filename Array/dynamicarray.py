import ctypes

class DynamicArray(object):


    def __init__(self):
        self.eleCount = 0
        self.capacity = 1
        self.arr = self.makeArray(self.capacity)

    def __length__(self):
        return self.eleCount

    def getItem(self, k):
        if not 0 <= k < self.eleCount:
            return IndexError('Index Out of Bounds')

        return self.arr[k]

    def append(self, ele):
        if self.eleCount == self.capacity:
            self._resize(2*self.capacity)

        self.arr[self.eleCount] = ele
        self.eleCount += 1

    def _resize(self, newCap):
        tmpArr = self.makeArray(newCap)

        for i in range(self.eleCount):
            tmpArr[i] = self.arr[i]

        self.arr = tmpArr
        self.capacity = newCap

    def makeArray(self, newCap):
        return (newCap * ctypes.py_object)()

Array = DynamicArray()
Array.append(1)

print(Array.__length__())

Array.append(2)
print(Array.__length__())
