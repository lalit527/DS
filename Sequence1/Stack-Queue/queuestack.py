from stack import Stack 
from collections import deque

class QueueStack:
    def __init__(self):
        self.stack = Stack()

    def printStack(self):
        self.stack.printStack()

    def enqueue(self, n):
        self.stack.push(n)

    def dequeue(self):
        # n = self.stack.pop()
        if self.stack.isEmpty():
            print('Stack is Empty')
            return
        n = self.stack.pop()
        if self.stack.isEmpty():
            print('Element is', n)
        else:
            self.dequeue()
            print('Saved',n)
            self.stack.push(n)
        

q = QueueStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printStack()
q.dequeue()
# print(q.dequeue())
# print(q.dequeue())
print('#######')
print(q.printStack())
# q.printStack()
