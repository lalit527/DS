from collections import deque
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert_root(self, data):
    node = Node(data)
    if self.root is None:
      self.root = node

  def insert(self, root, data):
    self._insert(root, data)

  def _insert(self, root, data):
    if root:
      if root.data > data:
        if root.left is None:
          root.left = Node(data)
        else:
          self.insert(root.left, data)
      else:
        if root.right is None:
          root.right = Node(data)
        else:
          self.insert(root.right, data)

  def search(self, data):
    root = self.root
    self._search(root, data)

  def _search(self, root, data):
    if root is None or root.data == data:
      return root
    
    if root.data > data:
      return self._search(root.left, data)
    elif root.data < data:
      return self._search(root.right, data)

  def successor(self, root):
    tmp = root.right
    while tmp.left is not None:
      tmp = tmp.left
    return tmp

  def delete(self, data):
    root = self.root
    self._delete(root, data)

  def _delete(self, root, data):
    if root is None:
      return root
    
    if root.data > data:
      root.left = self._delete(root.left, data)
    elif root.data < data:
      root.right = self._delete(root.right, data)
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
        tmp = self.successor(root)
        root.data = tmp.data
        root.right = self._delete(root.right, tmp.data)
    
    return root

  def print_level(self):
    root = self.root
    Q = deque()
    Q.append(root)
    while len(Q) > 0:
      node = Q.popleft()
      print(node.data)
      if node.left is not None:
        Q.append(node.left)
      if node.right is not None:
        Q.append(node.right)


def main():
  t = BinarySearchTree()
  t.insert_root(5)
  t.insert(t.root, 3)
  t.insert(t.root, 4)
  t.insert(t.root, 2)
  t.insert(t.root, 7)
  t.insert(t.root, 6)
  t.insert(t.root, 9)
  print(t.search(8))
  t.delete(7)
  t.print_level()


if __name__ == "__main__":
  main()