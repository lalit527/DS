from stack import Stack

class QueueWithStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def push(self, n):
        self.stack1.push(n)

    def pop(self):
        if self.stack2.isEmpty():
            while(self.stack1.isEmpty() == False):
                self.stack2.push(self.stack1.pop())

        return  self.stack2.pop()
    

q = QueueWithStack()
q.push(1)
q.push(2)
print(q.pop())
print(q.pop())