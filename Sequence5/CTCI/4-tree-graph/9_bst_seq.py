from main.binary_search_tree import BinarySearchTree

def weave_list(first, second, results, prefix):
  if len(first) == 0 or len(second) == 0:
    result = prefix[:]
    result.extend(first)
    result.extend(second)
    results.append(result)
    return
  
  head_first = first[0:1]
  prefix.append(head_first)
  weave_list(first, second, result, prefix)
  prefix.pop()

  head_second = second[0:1]
  prefix.append(head_second)
  weave_list(first, second, results, prefix)
  prefix.pop()
  


def all_sequence(root):
  result = []
  if root is None:
    result.append([])
    return result
  
  prefix = []
  prefix.append(root.data)
  left_seq = all_sequence(node.left)
  right_seq = all_sequence(node.right)

  for left in left_seq:
    for right in right_seq:
      weaved = []
      weave_list(left, right, weaved, prefix)
      result.append(weaved)
  return result

def main():
  t = BinarySearchTree()
  t.insert_root(5)
  t.insert(t.root, 3)
  t.insert(t.root, 4)
  t.insert(t.root, 2)
  t.insert(t.root, 7)
  t.insert(t.root, 6)
  t.insert(t.root, 9)
  all_seq = all_sequence(t.root)

if __name__ == "__main__":
  main()