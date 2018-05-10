class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
  
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
      tmp.parent = node
    
    return tmp
  
  def insertRight(self, node, n):
    tmp = None
    if node is None:
      return node
    
    if node.right is None:
      tmp = Node(n)
      node.right = tmp
      tmp.parent = node
    
    return tmp
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.data)
      self._inorder(root.right)


def getLCA(root, node1, node2):
  level1 = getLevel(root, node1)
  level2 = getLevel(root, node2)
  if (level1 > level2):
    length = level1 - level2
    while length > 0:
      node1 = node1.parent
      length -= 1
  else:
    length = level2 - level1
    while length > 0:
      node2 = node2.parent
      length -= 1
  while node1 is not None and node2 is not None:
    if node1 == node2:
      return node1
      break;
    else:
      node1 = node1.parent
      node2 = node2.parent
    
  return node1


def getLevel(root, node):
  level = 0
  return _level(root, node, level)

def _level(root, node, level):
  if root is None:
    return 0
  if root.data == node.data:
    return level
  l = _level(root.left, node, level+1)
  r = _level(root.right, node, level+1)

  if l > 0:
    return l

  if r > 0:
    return r
    
  return -1

t = Tree(5)
left = t.insertLeft(t.root, 4)
right = t.insertRight(t.root, 7)
t.inorder()
node = getLCA(t.root, left, right)
print(node.data if node else None)