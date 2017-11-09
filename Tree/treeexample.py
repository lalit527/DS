class Node:
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b 
b.nextnode = c
c.nextnode = d

print(b.nextnode.nextnode.value)

def printNode(node):
    while node:
        print(node.value)
        node = node.nextnode

def rev(node):
    
class Node:
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b 
b.nextnode = c
c.nextnode = d

#print(b.nextnode.nextnode.value)
printNode(a)
