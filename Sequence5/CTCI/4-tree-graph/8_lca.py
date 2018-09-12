from main.binarytree import BinaryTree

# With Link to parent Node
def depth(root):
  depth = 0
  while root is not None:
    root = root.parent
    depth += 1
  return depth

def go_up_by(root, n):
  while n > 0 and root is not None:
    root = root.parent
    n -= 1
  return root

def common_anchestor(p, q):
  delta = depth(p) - depth(q)
  first = p if delta >= 0 else q
  second = q if delta <= 0 else p
  if delta > 0:
    go_up_by(p, delta)
  else:
    go_up_by(q, abs(delta))
  
  while first != second and first is not None or second is not None:
    first = first.parent
    second = second.parent
  
  return None if first is None or second is None else first

  
# without Link to parent Node
def common_anchestor_3(root, p, q):
  if root is None:
    return None
  
  if root == p and root == q:
    return root
  
  x = common_anchestor(root.left, p, q)
  if x != None and x != p and x != q:
    return x

  y = common_anchestor(root.right, p, q)
  if y != None and y != p and y != q:
    return y
  
  if x != None and y != None:
    return root

  
# Without Link - Checks for node in tree

class Result:
  def __init__(self, node, isAnchestor):
    self.node = node
    self.isAnchestor = isAnchestor

def common_anchestor_4(root, p, q):
  r = common_anchestor_4_helper(root, p, q):
  if r.isAnchestor:
    return r.node
  return None

def common_anchestor_4_helper(root, p, q):
  if root is None:
    return Result(None, false)
  
  if root == p and root == q:
    return Result(root, True)

  rx = common_anchestor_4_helper(root.left, p, q)
  if rx.isAnchestor:
    return rx

  ry = common_anchestor_4_helper(root.right, p, q)
  if ry.isAnchestor:
    return ry

  if rx.node != None and ry.node != None:
    return Result(root, True)
  elif root == p or root == q:
    isAnchestor = rx.node != None or ry.node != None
    return Result(root, isAnchestor)
  else:
    return Result(rx.node if rx.node else ry.node, False)
  





def main():
  BT = BinaryTree()
  n1 = BT.insertLeft(1)
  n2 = BT.insertLeft(2, n1)
  n3 = BT.insertRight(3, n1)
  BT.print_level()

if __name__ == "__main__":
  main()