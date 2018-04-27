from collections import deque
from trees import Tree

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def inOrderRec(root):
    stack = deque()
    current = root
    done = False
    while not done:
        if current.left != None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.data)

                current = current.right
            
            else:
                done = True

def inOrderRec2(root):
    stack = deque()
    tmp = root
    stack.append(tmp)
    while stack.__len__() > 0:
        tmp = stack[-1]
        if tmp.left != None:
            stack.append(tmp.left)
            tmp = tmp.left
        else:
        
        data = stack.pop()
        print(data.data)
        if tmp.right != None:
            stack.ap

t = Tree(5)
t.insertLeft(2)
t.insertRight(7)
root = t.getRoot()
inOrder(root)
inOrderRec(root)