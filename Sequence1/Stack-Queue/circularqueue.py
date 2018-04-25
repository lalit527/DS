class DoubleQueue:
    def __init__(self, capacity = 16):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.size = 0 
        self.queue = [None] * self.capacity

    def enqueue(self, n):
        if self.front == -1:
            self.front = 0
        elif self.isFull():
            print('We will check this')
        self.rear = (self.rear + 1) % self.capacity
        print(self.rear)
        self.queue[self.rear] = n
        print(self.queue)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return Exception("Queue is Empty")
        else:
            tmp = self.front
            self.front = (self.front + 1) % self.capacity
            return self.queue[tmp]

    def isFull(self):
        tmp = (self.rear+1) % self.capacity
        return self.rear+1 == self.front

    def isEmpty(self):
        return self.front > self.rear

queue = DoubleQueue(1)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())