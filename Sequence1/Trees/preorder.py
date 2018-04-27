from collections import deque
from trees import Tree

def preOrder(root):
    if root != None:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def preOrderItr(root):
    stack = deque()
    current = root
    done = False
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        print(node.data)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)

t = Tree(5)
t.insertLeft(2)
t.insertRight(7)
# t.getLeftChild().insertLeft(3)
root = t.getRoot()
# preOrder(root)
preOrderItr(root)