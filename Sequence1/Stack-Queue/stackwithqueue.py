class QueueWithStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, n):
        self.stack1.append(n)

    def pop(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)-1, -1, -1):
                self.stack2.append(self.stack1[i])

        return  self.stack2.pop()
    

q = QueueWithStack()
q.push(1)
q.push(2)
print(q.pop())
print(q.pop())