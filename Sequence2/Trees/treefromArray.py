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


ino = ['D', 'B' ,'E', 'A', 'F', 'C']
pro = ['A', 'B', 'D', 'E', 'C', 'F']
tree = buidTree(ino, pro)
tree.inorder()