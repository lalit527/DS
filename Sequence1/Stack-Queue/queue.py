class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, n):
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue.append(n)

    def dequeue(self):
        if self.isEmpty():
            return Exception("Queue Is Empty")
        tmp = self.front
        self.front += 1
        return self.queue[tmp]

    def peek(self):
        if self.isEmpty():
            return Exception("Queue Is Empty")
        return self.queue[self.front]

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
    
