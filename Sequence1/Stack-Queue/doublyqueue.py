class DoubleQueue:
    def __init__(self, capacity = 16):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.size = 0 
        self.queue = [None] * self.capacity

    def enqueueEnd(self, n):
        if self.front == -1:
            self.front = 0
        if self.size == self.capacity:
            self.increaseCapacity()
        self.rear += 1
        self.queue[self.rear] = n
        self.size += 1

    def dequeueFront(self):
        if self.isEmpty():
            return Exception("Queue Is Empty")
        tmp = self.front
        self.front += 1
        return self.queue[tmp]

    def enqueueFront(self, n):
        if self.front == -1:
            self.front = 0
        if self.size == self.capacity:
            self.increaseCapacity()
        for i in range(len(self.queue)-2, -1, -1):
            self.queue[i+1] = self.queue[i]
        self.queue[0] = n
        self.rear += 1
        self.size += 1

    def dequeueEnd(self):
        if self.isEmpty():
            return Exception("Queue Is Empty")
        tmp = self.rear
        self.rear -= 1
        return self.queue[tmp]

    def peek(self):
        if self.isEmpty():
            return Exception("Queue Is Empty")
        return self.queue[self.front]

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def increaseCapacity(self):
        self.capacity *= 2
        tmpArr = [None] * self.capacity
        for i in range(len(self.queue)):
            tmpArr[i] = self.queue[i]
        self.queue = tmpArr
    
    def checkQueue(self):
        for i in self.queue:
            print(i)



queue = DoubleQueue(1)
queue.enqueueEnd(1)
queue.enqueueEnd(2)
queue.enqueueEnd(3)
queue.enqueueFront(4)
# queue.checkQueue()
print(queue.dequeueEnd())
print(queue.dequeueFront())
# print(queue.dequeueFront())
    
