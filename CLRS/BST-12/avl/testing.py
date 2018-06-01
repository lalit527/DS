class BSTNode:
  def __init__(self, parent, key):
    self.key = key
    self.parent = parent
    self.left = None
    self.right = None

  def _str(self):
    print("=====+Start+==================")
    label = str(self.key)
    print(label, len(label))
    if self.left is None:
      left_lines, left_pos, left_width = [], 0, 0
    else:
      left_lines, left_pos, left_width = self.left._str()
    if self.right is None:
      right_lines, right_pos, right_width = [], 0, 0
    else:
      right_lines, right_pos, right_width = self.right._str()
    middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
    print('middle', middle, right_pos, left_width, left_pos)
    pos = left_pos + middle // 2
    print('pos', pos)
    width = left_pos + middle + right_width - right_pos
    print('width', width, left_lines, right_lines)
    while len(left_lines) < len(right_lines):
      left_lines.append(' ' * left_width)
    while len(right_lines) < len(left_lines):
      right_lines.append(' ' * right_width)
    if (middle - len(label)) % 2 == 1 and self.parent is not None and \
      self is self.parent.left and len(label) < middle:
      label += '.'
    label = label.center(middle, '.')
    if label[0] == '.':
      label = ' ' + label[1:]
    if label[-1] == '.': 
      label = label[:-1] + ' '
    lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
             ' ' * left_pos + '/' + ' ' * (middle - 2) + 
             '\\' + ' ' * (right_width - right_pos)] + \
      [left_line + ' ' * (width - left_width - right_width) + right_line
        for left_line, right_line in zip(left_lines, right_lines)]
    print('returning this', lines, pos, width)
    print("=====+End+==================")
    return lines, pos, width

  def __str__(self):
    return '\n'.join(self._str()[0])

  def insert(self, node):
    print('self', self, 'node', node)
    if node is None:
      return
    if node.key < self.key:
      if self.left is None:
        node.parent = self
        self.left = node
      else:
        self.left.insert(node)
    else:
      if self.right is None:
        node.parent = self
        self.right = node
      else:
        self.right.insert(node)

class BST:
  def __init__(self, klass = BSTNode):
    self.root = None
    self.klass = klass

  def __str__(self):
    if self.root is None:
      return '<empty tree>'
    return str(self.root)

  def insert(self, k):
    node = self.klass(None, k)
    if self.root is None:
      self.root = node
    else:
      self.root.insert(node)
    return node

tree = BST()
arr = [50, 30, 40, 20, 70, 60, 90]
for item in arr:
  tree.insert(item)
# print(tree.root.left.left)