from collections import deque
from binary_search_tree import BinarySearchTree

def in_order(root):
  if root:
    in_order(root.left)
    print(root.data)
    in_order(root.right)

def pre_order(root):
  if root:
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
  if root:
    post_order(root.left)
    post_order(root.right)
    print(root.data)

# Traversing the tree without recurssion

def pre_order_itr(root):
  S = deque()
  current = root
  done = False
  S.append(root)
  while len(S) > 0:
    node = S.pop()
    print(node.data)
    if node.right:
      S.append(node.right)
    if node.left:
      S.append(node.left)

def in_order_itr(root):
  S = deque()
  current = root
  done = False
  while not done:
    if current is not None:
      S.append(current)
      current = current.left
    else:
      if len(S) > 0:
        current = S.pop()
        print(current.data)
        current = current.right
      else:
        done = True

def peek(stack):
  if len(stack) > 0:
      return stack[-1]
  return None

def post_order_itr(root):
  S = deque()
  current = root
  done = False
  while not done:
    while current:
      if current.right:
        S.append(current.right)
      S.append(current)
      current = current.left
      
    current = S.pop()

    if current.right and peek(S) == current.right:
      tmp = S.pop()
      S.append(current)
      current = current.right
    else:
      print(current.data)
      current = None
    
    if len(S) <= 0:
      done = True


def main():
  t = BinarySearchTree()
  t.insert_root(5)
  t.insert(t.root, 3)
  t.insert(t.root, 4)
  t.insert(t.root, 2)
  t.insert(t.root, 7)
  t.insert(t.root, 6)
  t.insert(t.root, 9)
  # print(t.search(8))
  # t.delete(7)
  post_order_itr(t.root)


if __name__ == "__main__":
  main()