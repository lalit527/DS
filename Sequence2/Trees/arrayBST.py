from binarysearchtree import BinarySearchTree, Node, inorder

def createBST(arr):
  node = _createBST(arr, 0, len(arr) - 1)
  b = BinarySearchTree(node)
  return b

def _createBST(arr, start, end):
  
  if start > end:
    return None
  
  mid = (start + end) // 2 
  node = Node(arr[mid])
  node.left = _createBST(arr, start, mid - 1)
  node.right = _createBST(arr, mid + 1, end)

  return node

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = createBST(arr)
inorder(t.root)