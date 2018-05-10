from binarytree import BinaryTree, Node
class Index:
  def __init__(self):
    self.value = None

def search(ino, start, end, data):
  for i in range(start, end+1):
    if ino[i] == data:
      return i

def buidTree(ino, pro):
  t = BinaryTree()
  index = Index()
  index.value = 0
  start = 0
  end = len(ino) - 1
  root = _buildTree(ino, pro, start, end, index)
  t.root = root
  return t

def _buildTree(ino, pro, start, end, index):
  if start > end:
    return None

  node = Node(pro[index.value])
  index.value += 1

  if start == end:
    return node

  inIndex = search(ino, start, end, node.data)
  node.left = _buildTree(ino, pro, start, inIndex - 1, index)
  node.right = _buildTree(ino, pro, inIndex + 1, end, index)

  return node

def buildTreeInPo(ino, poo):
  index = Index()
  length = len(ino)
  start = 0
  end = length - 1
  index.value = end
  root = _buildTreeInPo(ino, poo, start, end, index)
  t = BinaryTree()
  t.root = root
  return t

def _buildTreeInPo(ino, poo, start, end, index):
  if start > end:
    return None
  
  node = Node(poo[index.value])
  index.value -= 1

  if start == end:
    return node
  
  inIndex = search(ino, start, end, node.data)

  node.right = _buildTreeInPo(ino, poo, inIndex + 1, end, index)
  node.left = _buildTreeInPo(ino, poo, start, inIndex - 1, index)

  return node

ino = ['D', 'B' ,'E', 'A', 'F', 'C']
pro = ['A', 'B', 'D', 'E', 'C', 'F']
tree = buidTree(ino, pro)
tree.inorder()

ino = [4, 8, 2, 5, 1, 6, 3, 7]
poo = [8, 4, 5, 2, 6, 7, 3, 1]
t = buildTreeInPo(ino, poo)
t.inorder()