from collections import defaultdict
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def count_paths_with_sum(root, target):
  if root is None:
    return 0
  
  paths_from_root = count_paths_with_sum_from_node(root, target, 0)

  paths_on_left = count_paths_with_sum(root.left, target)
  paths_on_right = count_paths_with_sum(root.right, target)

  return paths_from_root + paths_on_left + paths_on_right

def count_paths_with_sum_from_node(node, target, current):
  if node is None:
    return 0
  
  current += node.data
  total_paths = 0
  if current == target:
    total_paths += 1

  total_paths += count_paths_with_sum_from_node(node.left, target, current)
  total_paths += count_paths_with_sum_from_node(node.right, target, current)

  return total_paths


## Solution 2
def count_paths_with_sum_2(root, target):
  path_count = defaultdict(lambda: 0)
  return _count_paths_with_sum_2(root, target, 0, path_count)

def _count_paths_with_sum_2(root, target, running_sum, path_count):
  if root is None:
    return 0

  running_sum += root.data
  sum = running_sum - target
  total_paths = path_count[sum]

  if running_sum == target:
    total_paths += 1
  
  increment_hash(path_count, running_sum, 1)
  total_paths += _count_paths_with_sum_2(root.left, target, running_sum, path_count)
  total_paths += _count_paths_with_sum_2(root.right, target, running_sum, path_count)
  return total_paths


def increment_hash(hash, key, delta):
  new_count = hash[key] + delta
  if new_count == 0:
    del hash[key]
  else:
    hash[key] = new_count


def main():
  # root = Node(5)
  # root.left = Node(3)
  # root.right = Node(1)
  # root.left.left = Node(-8)
  # root.left.right = Node(8)
  # root.right.left = Node(2)
  # root.right.right = Node(6)

  root = Node(10)
  root.left = Node(5)
  root.right = Node(3)
  root.left.left = Node(3)
  root.left.right = Node(1)
  root.right.right = Node(11)
  root.left.left.left = Node(3)
  root.left.left.left = Node(-2)
  root.left.right.right = Node(2)

  print(count_paths_with_sum_2(root, 8))

if __name__ == "__main__":
  main()