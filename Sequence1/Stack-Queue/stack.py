class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, n):
        self.top += 1
        self.stack.append(n)
        
    
    def pop(self):
        if self.isEmpty():
            return Exception("Stack is empty") 
        tmp = self.top
        self.top -= 1
        return self.stack[tmp]
    
    def peek(self):
        if self.isEmpty():
            return Exception("Stack is empty") 
        else:
            return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def length(self):
        return self.top

    def printStack(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
    