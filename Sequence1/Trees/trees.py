class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, n):
        root = Node(n)
        self.root = root

    def insertLeft(self, root, n):
        if root.left == None:
            root.left = Node(n)
        else:
            tmp = Node(n)
            tmp.left = root.left
            slef.root.left = tmp

    def insertRight(self, root, n):
        if root.right == None:
            root.right = Node(n)
        else:
            tmp = Node(n)
            tmp.right = root.right
            root.right = tmp

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

'''
t = Tree(5)
t.insertLeft(2)
t.insertRight(7)
root = t.getRoot()
t.inOrder(root)
'''
