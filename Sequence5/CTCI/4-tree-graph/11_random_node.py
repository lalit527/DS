from random import randint

class TreeNode:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None
    self.size = 0

  def insert_inorder(self, d):
    if d <= self.data:
      if self.left is None:
        self.left = TreeNode(d)
      else:
        self.left.insert_inorder(d)
    else:
      if self.right is None:
        self.right = TreeNode(d)
      else:
        self.right.insert_inorder(d)
      
    self.size += 1
  
  def find(self, d):
    if d == self.data:
      return self
    elif d < self.data:
      if self.left:
        return self.left.find(d) 
    elif d > self.data:
      if self.right:
        return self.right.find(d) 
    
    return None

  def random_node(self):
    left_size = self.left.size if self.left else 0
    index = randint(self.size)
    if index == left_size:
      return self
    elif index < left_size:
      return self.left.random_node()
    else:
      return self.right.random_node()

  def get_inode(self, index):
    left_size = self.left.size if self.left else 0
    if index == left_size:
      return self
    elif index < left_size:
      return self.left.get_inode(index)
    else:
      return self.right.get_inode(index - (left_size + 1))
    

class Tree:
  def __init__(self):
    self.root = None
  
  def insert_inorder(self, value):
    if self.root is None:
      self.root = TreeNode(value)
    else:
      self.root.insert_inorder(value)
    
  def size(self):
   return self.root.size
  
  def get_random_node(self):
    if self.root is None:
      return None
    index = randint(1, self.size())
    return self.root.get_inode(index)

if __name__ == "__main__":
  tree = Tree()
  array = [1, 0, 6, 2, 3, 9, 4, 5, 8, 7]
  for x in array:
    tree.insert_inorder(x)
  d = tree.get_random_node().data
  print(d)
