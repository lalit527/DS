from main.binary_search_tree import Node, BinarySearchTree

MIN_VAL = float('-inf')

def get_height(root):
  if root is None:
    return 0
  return max(get_height(root.left), get_height(root.right)) + 1

def check_tree_balance(root):
  if root is None:
    return True
  
  height = get_height(root.left) - get_height(root.right)

  if abs(height) > 1:
    return False
  else:
    return check_tree_balance(root.left) and check_tree_balance(root.right)


def is_tree_balanced(root):
  if root is None:
    return -1

  left = is_tree_balanced(root.left)
  if left == MIN_VAL:
    return MIN_VAL
  
  right = is_tree_balanced(root.right)
  if right == MIN_VAL:
    return MIN_VAL
  
  height = left - right

  if abs(height) > 1:
    return MIN_VAL
  else:
    return max(left, right) + 1

def check_balance(root):
  return is_tree_balanced(root) != MIN_VAL
  


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
  print(check_balance(t.root))

if __name__ == "__main__":
  main()