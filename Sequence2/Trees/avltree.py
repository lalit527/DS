class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 1

class AvlTree:
  def __init__(self):
    self.root = None

  def height(self, node):
    if node is None:
      return 0
    return node.height

  def getBlance(self, node):
    if node is None:
      return 0

    return self.height(node.left) - self.height(node.right)

  def insert(self, node, key):
    if node is None:
      return Node(key)
    
    if key > node.key:
      node.right = self.insert(node.right, key)

    elif key < node.key:
      node.left = self.insert(node.left, key)

    else:
      return node

    node.height = 1 + max(self.height(node.left), self.height(node.right))

    balance = self.getBalance(node)

    if balance > 1 and key < node.left.key:
      return self.rightRotate(node)
    
    if balance > 1 and key > node.left.key:
      node.left = self.leftRotate(node.left)
      return self.rightRotate(node)

    if balance < -1 and key > node.right.key:
      return self.leftRotate(node)
    
    if balance < -1 and key < node.right.key:
      node.right = self.rightRotate(node.right)
      return self.leftRotate(node)

    return node

  def delete(self, root, key):
    if root is None:
      return root
    
    if root.data < key:
      root.right = self.delete(root.right, key)
    elif root.data > key:
      root.left = self.left(root.left, key)
    
    else:
      if root.right is None:
        tmp = root.left
        root = None
        return tmp
      
      elif root.left is None:
        tmp = root.right
        root = None
        return tmp

      else:
        tmp = self.getSuccessor(root.right)
        root.data = tmp.data
        self.delete(root.right, tmp.data)

    if root is None:
      return root

    root.height = 1 + max(self.height(root.left), self.height(root.right))

    balance = self.getBalance(root)

    if balance > 1 and key < root.left.key:
        return self.rightRotate(root)
      
    if balance > 1 and key > root.left.key:
      root.left = self.leftRotate(root.left)
      return self.rightRotate(root)

    if balance < -1 and key > root.right.key:
      return self.leftRotate(root)
    
    if balance < -1 and key < root.right.key:
      root.right = self.rightRotate(root.right)
      return self.leftRotate(root)

    return root


  def leftRotate(self, root):
    y = node.right
    tmp = y.left

    y.left = Node
    node.right = tmp

    node.height = 1 + max(self.height(node.left), self.height(node.right))
    y.height = 1 + max(self.height(y.left), self.height(y.right))
    
    return y

  def rightRotate(self, node):
    x = node.left
    tmp = x.right
    
    x.right = node
    node.left = tmp
    
    node.height = 1 + max(self.height(node.left), self.height(node.right))
    x.height = 1 + max(self.height(x.left), self.height(x.right))
    
    return x



t = AvlTree()