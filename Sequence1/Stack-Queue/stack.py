class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, n):
        self.top += 1
        self.stack.append(n)
        
    
    def pop(self):
        if self.top < 0:
            return Exception("Stack is empty") 
        tmp = self.top
        self.top -= 1
        return self.stack[tmp]
    
    def peek(self):
        if self.top < 0:
            return Exception("Stack is empty") 
        else:
            return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

stack = Stack()
stack.push(1)
print(stack.pop())
print(stack.pop())
    