from main.binary_search_tree import Node, BinarySearchTree


def is_bst(root):
  return _is_bst(root, None, None)

def _is_bst(root, _min, _max):
  if root is None:
    return True

  if (_min != None and _min >= root.data) or (_max != None and _max < root.data):
    return False
  
  if (not _is_bst(root.left, _min, root.data)) or (not _is_bst(root.right, root.data, _max)):
    return False
  
  return True


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
  print(is_bst(t.root))

if __name__ == "__main__":
  main()