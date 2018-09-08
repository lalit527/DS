from main.binary_search_tree import Node, BinarySearchTree

def make_tree(arr):
  start = 0
  end = len(arr) - 1
  B = BinarySearchTree()
  B.root = _make_tree(arr, start, end)
  return B

def _make_tree(arr, start, end):
  if start <= end:
    mid = (start + end) // 2
    node = Node(arr[mid])
    node.left = _make_tree(arr, start, mid - 1)
    node.right = _make_tree(arr, mid + 1, end)
    return node

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  bst = make_tree(arr)
  bst.print_level()
