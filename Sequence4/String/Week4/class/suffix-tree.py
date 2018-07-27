class SuffixTreeNode:
  def __init__(self, parent, children, depth, start, end):
    self.parent = parent
    self.children = children
    self.depth = depth
    self.start = start
    self.end = end

def lcp_suffix(S, i, j, equal):
  n = len(S)
  lcp = max(0, equal)
  while i + lcp < n and j + lcp < n:
    if S[i + lcp] == S[j + lcp]:
      lcp += 1
    else:
      break
  return lcp

def invert_suffix_array(order):
  n = len(order)
  pos = [None] * n
  for i in range(n):
    pos[order[i]] = i
  return pos

def compute_lcp_array(S, order):
  n = len(S)
  lcp_array = [None] * n
  lcp = 0
  pos_inorder = invert_suffix_array(order)
  suffix = order[0]
  for i in range(n):
    order_index = pos_inorder[suffix]
    if order_index == n - 1:
      lcp = 0
      suffix = (suffix + 1) % n
      continue
    next_suffix = order[order_index + 1]
    lcp = lcp_suffix(S, suffix, next_suffix, lcp - 1)
    lcp_array[order_index] = lcp
    suffix = (suffix + 1) % n
  return lcp_array

def build_suffix_tree_from_array(S, order, lcp_array):
  n = len(S)
  root = SuffixTreeNode(None, {}, 0, -1, -1)
  lcp_prev = 0
  cur_node = root
  for i in range(n):
    suffix = order[i]
    while cur_node.depth > lcp_prev:
      cur_node = cur_node.parent
    if cur_node.depth == lcp_prev:
      cur_node = create_new_leaf(cur_node, S, suffix)
    else:
      edge_start = order[i - 1] + cur_node.depth
      offset = lcp_prev - cur_node.depth
      mid_node = break_edge(cur_node, S, edge_start, offset)
      cur_node = create_new_leaf(mid_node, S, suffix)
    if i < n - 1:
      lcp_prev = lcp_array[i]
  return root

def create_new_leaf(node, S, suffix):
  n = len(S)
  leaf = SuffixTreeNode(node, {}, n - suffix, suffix + node.depth, n - 1)
  node.children[S[leaf.start]] = leaf
  return leaf

def break_edge(node, S, start, offset):
  start_char = S[start]
  mid_char = S[start + offset]
  mid_node = SuffixTreeNode(node, {}, node.depth + offset, start, start + offset + 1)
  mid_node.children[mid_char] = node.children[start_char]
  node.children[start_char].parent = mid_node
  node.children[start_char].start += offset
  node.children[start_char] = mid_node
  return mid_node

def print_output(root):
  # print(root.children)
  for child in root.children:
    print(root.start, '->', root.end, '->', root.depth, '--->>', root.children)
    print_output(root.children[child])


def main():
  S = "GTAGT$"
  order = [5, 2, 3, 0, 4, 1]
  lcp = [0, 0, 2, 0, 1]
  lcp_array = compute_lcp_array(S, order)
  root = build_suffix_tree_from_array(S, order, lcp_array)
  print_output(root)

if __name__ == "__main__":
  main()