class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None

class BST:
  def __init__(self, data):
    self.root = Node(data)
  
  def insert(self, parent, data):
    if parent:
      if parent.data > data:
        if parent.left is None:
          node =  Node(data)
          parent.left = Node(data)
          node.parent = parent
        else:
          parent.left = self.insert(root.left, data)
      else:
        if parent.right is None:
          node =  Node(data)
          parent.right = Node(data)
          node.parent = parent



def get_successor(root):
  if root is None:
    return root
  
  if root.right is not None:
    tmp = root.right
    while tmp.left is not None:
      tmp = tmp.left
    return tmp
  else:
    q = root
    x = q.parent
    while x is not None and x.left != q:
      q = x
      x = x.parent
    return x




def main():
  t = BinarySearchTree()
  t.insert_root(5)
  t.insert(t.root, 3)
  t.insert(t.root, 4)
  t.insert(t.root, 2)
  t.insert(t.root, 7)
  t.insert(t.root, 6)
  t.insert(t.root, 9)
  t.insert(t.root, 10)
  t.insert(t.root, 14)
  t.insert(t.root, 12)
  t.insert(t.root, 15)
  print(get_successor(t.root))

if __name__ == "__main__":
  main()