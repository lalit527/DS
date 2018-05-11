from binarysearchtree import BinarySearchTree, Node
from collections import deque

def checkSumPair(root, target):
  stack1 = deque()
  stack2 = deque()
  done1 = False
  done2 = False
  val1 = 0
  val2 = 0
  curr1 = root
  curr2 = root
  while(1):
    while(done1 == False):
      if curr1 is not None:
        stack1.append(curr1)
        curr1 = curr1.left
      else:
        if len(stack1) <= 0:
          done1 = True
        else:
          curr1 = stack1.pop()
          val1 = curr1.data
          curr1 = curr1.right
          done1 = True

    while done2 == False:
      if curr2 is not None:
        stack2.append(curr2)
        curr2 = curr2.right
      else:
        if len(stack2) <= 0:
          done2 = True
        else:
          curr2 = stack2.pop()
          val2 = curr2.data
          curr2 = curr2.left
          done2 = True
    if ((val1 != val2) and
       (val1 + val2) == target):
      print(val1, val2, target)
      return True
    elif (val1 + val2 ) < target:
      done1 = True
    elif (val1 + val2) > target:
      done2 = False 

    if val1 >= val2:
      return False

s = BinarySearchTree(5)
s.insert(s.root, 3)
s.insert(s.root, 4)
s.insert(s.root, 2)
s.insert(s.root, 7)
s.insert(s.root, 6)
s.insert(s.root, 9)
print(checkSumPair(s.root, 16))