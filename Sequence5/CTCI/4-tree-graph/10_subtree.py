from main.binary_search_tree import BinarySearchTree

# Simple with pre-order traversal
def contains_tree(t1, t2):
  s1 = []
  s2 = []
  get_order_string(t1.root, s1)
  get_order_string(t2.root, s2)
  s1 = ' '.join(s1)
  s2 = ' '.join(s2)
  return s1.find(s2) != -1

def get_order_string(t, s):
  if t is None:
    s.append("X")
    return
  s.append(str(t.data))
  get_order_string(t.left, s)
  get_order_string(t.right, s)


# Search through large tree
def contains_tree_search(t1, t2):
  if t2 is None:
    return True
  return sub_tree(t1.root, t2.root)

def sub_tree(r1, r2):
  if r1 is None:
    return False
  elif r1.data == r2.data and (match_tree(r1, r2)):
    return True
  
  return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)


def match_tree(r1, r2):
  if r1 is None and r2 is None:
    return True
  elif r1 is None or r2 is None:
    return False
  elif r1.data != r2.data:
    return False
  else:
    return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)



def main():
  t = BinarySearchTree()
  t.insert_root(5)
  t.insert(t.root, 3)
  t.insert(t.root, 4)
  t.insert(t.root, 2)
  t.insert(t.root, 7)
  t.insert(t.root, 6)
  t.insert(t.root, 9)

  t1 = BinarySearchTree()
  t1.insert_root(7)
  t1.insert(t1.root, 6)
  t1.insert(t1.root, 9)

  print(contains_tree_search(t, t1))


if __name__ == "__main__":
  main()