from binarysearchtree import BinarySearchTree
from collections import deque

def findPair(root, n):
  stack1 = deque()
  stack2 = deque()
  curr1 = root
  curr2 = root
  done = False
  stack1.append(curr1)
  while curr1.left is not None:
    stack1.append(curr1.left)
    curr1 = curr1.left
  
  while curr2.right is not None:
    stack2.append(curr2.right)
    curr2 = curr2.right
  
  while not done:
    if len(stack1) == 0 or len(stack2) == 0:
      return None
    
    dl = stack1.pop()
    dr = stack2.pop()
    
    if dl.data + dr.data == n:
      done = True
      return [dl.data, dr.data]
    elif dl.data + dr.data > n:
      if dr.left:
        stack2.append(dr.left)
    elif dl.data + dr.data < n:
      if dl.right:
        stack1.append(dl.right)
    if len(stack1) == 0 and len(stack2) == 0:
      done = True
  
  print(stack1)
  print(stack2)

  

t = BinarySearchTree(5)
t.insert(t.root, 3)
t.insert(t.root, 4)
t.insert(t.root, 2)
t.insert(t.root, 7)
t.insert(t.root, 6)
t.insert(t.root, 9)
print(findPair(t.root, 16))