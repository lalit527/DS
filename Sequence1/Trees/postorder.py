from collections import deque
from trees import Tree

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postorderItr(root):
    stack = deque()
    current = root
    done = False
    while not done:
        while current:
            if current.right is not None:
                stack.append(current.right)
            stack.append(current)

            current = current.left
        current = stack.pop()

        if (current.right is not None and
            peek(stack) == current.right):
            stack.pop()
            stack.append(current)
            current = current.right

        else:
            print(current.data)
            current = None

        if len(stack) <= 0:
            done = True



        

t = Tree(5)
t.insertLeft(2)
t.insertRight(7)
# t.getLeftChild().insertLeft(3)
root = t.getRoot()
# preOrder(root)
postorderItr(root)