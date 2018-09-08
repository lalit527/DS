from collections import deque

class Node:
  def __init__(self, data):
    self.parent = None
    self.data = data
    self.children = []

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, data, parent = None):
    node = Node(data)
    if parent is not None:
      parent.children.append(node)
      node.parent = parent
    elif parent is None and self.root is None:
      self.root = node
    else:
      raise Exception("Invalid Parent Reference")
    
    return node
  
  def search(self, data):
    root = self.root
    return self._search(root, data)
  
  def _search(self, root, data):
    Q = deque()
    Q.append((root, -1))
    while len(Q) > 0: 
      front = Q.popleft()
      if front[0].data == data:
        return front
      for index, child in enumerate(front[0].children):
        Q.append((child, index))
    return (None, None)

  def delete(self, data):
    root = self.root
    result = self._search(root, data)
    self._delete(result)

  def _delete(self, result):
    if result[0] is None:
      raise Exception("Data not in Tree")
    if result[1] > -1:
      index = result[1]
      node = result[0]
      print(index, node.data)
      if len(node.children) > 0:
        if index == 0:
          parent = node.parent
        else:
          parent = node.parent.children[index - 1]
        for child in node.children:
          parent.children.append(child)
          child.parent = parent
      node.parent.children.remove(node) 
    else:
      node = result[0]
      if len(node.children) > 0:
        node.data = node.children[0].data
        self._delete((node.children[0], 0))
      else:
        self.root = None

  def print_tree(self):
    root = self.root
    self._print_tree(root)

  def _print_tree(self, root):
    if root is not None:
      print('Parent {} and child {}'.format(root.parent.data if root.parent else None, root.data))
      for child in root.children:
        self._print_tree(child)


def main():
  T = Tree()
  n1 = T.insert(1, None)
  n2 = T.insert(2, n1)
  n3 = T.insert(3, n1)
  n4 = T.insert(4, n1)
  n5 = T.insert(5, n1)
  n6 = T.insert(6, n1)
  n51 = T.insert(7, n5)
  n52 = T.insert(8, n5)
  n53 = T.insert(9, n5)
  n54 = T.insert(10, n5)
  n41 = T.insert(41, n4)
  n411 = T.insert(411, n41)
  n21 = T.insert(21, n2)
  T.delete(1)
  T.print_tree()

if __name__ == "__main__":
  main()

    
