class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, n):
        root = Node(n)
        self.root = root

    def insertLeft(self, n):
        if self.root.left == None:
            self.root.left = Tree(n)
        else:
            tmp = Node(n)
            tmp.left = self.root.left
            slef.root.left = tmp

    def insertRight(self, n):
        if self.root.right == None:
            self.root.right = Node(n)
        else:
            tmp = Node(n)
            tmp.right = self.root.right
            self.root.right = tmp

    def getRoot(self):
        return self.root
    
    def getLeftChild(self):
        return self.root.left

    def getRightChild(self):
        return self.root.right

t = Tree(5)
t.insertLeft(2)
print(t.getRoot().left)
# print(t.getLeftChild().left.data)