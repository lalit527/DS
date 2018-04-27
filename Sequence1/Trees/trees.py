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
            self.root.left = Node(n)
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

    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def preOrder(self, root):
        if root != None:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

t = Tree(5)
t.insertLeft(2)
root = t.getRoot()
t.inOrder(root)
print('#######################')
t.preOrder(root)
print('#######################')
t.postOrder(root)
# print(t.getLeftChild().left.data)