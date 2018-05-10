class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.next = None

class Tree:
  def __init__(self, data):
    self.root = Node(data)
  
  def insertLeft(self, node, n):
    tmp = None
    if node is None:
      return node
    
    if node.left is None:
      tmp = Node(n)
      node.left = tmp
    
    return tmp
  
  def insertRight(self, node, n):
    tmp = None
    if node is None:
      return node
    
    if node.right is None:
      tmp = Node(n)
      node.right = tmp
    
    return tmp
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.data)
      self._inorder(root.right)


# Methods start from here
def nextNode(root):
  if root is None:
    return root
  print(root.next.data)  


def getNextNode(root):
  tmp = root.next
  while tmp is not None:
    if tmp.left is not None:
      return tmp.left
    if tmp.right is not None:
      return tmp.right
    tmp = tmp.next
  return tmp

def connectLevel(root):
  if root is None:
    return root
  if root.next is not None:
    connectLevel(root.next)
  if root.left is not None:
    if root.right is not None:
      root.left.next = root.right
      root.right.next = getNextNode(root)
    else:
      root.left.next = getNextNode(root)
  elif root.right is not None:
    root.right = getNextNode(root)
  else:
    connectLevel(getNextNode(root))

t = Tree(5)
left = t.insertLeft(t.root, 4)
right = t.insertRight(t.root, 7)
l_1 = t.insertLeft(left, 2)
l_2 = t.insertRight(left, 3)
r_1 = t.insertLeft(right, 6)
r_2 = t.insertRight(right, 8)
connectLevel(t.root)
nextNode(t.root.left)