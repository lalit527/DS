from trees import Tree, Node
from collections import deque
def printLevel(root):
    if root is None:
        return root
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        root = queue.popleft()
        print(root.data)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
    

t = Tree(5)
t.insertLeft(2)
t.insertRight(4)
root = t.getRoot()
printLevel(root)
