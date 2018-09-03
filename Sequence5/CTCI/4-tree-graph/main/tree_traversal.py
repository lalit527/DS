def in_order(root):
  if root:
    self.in_order(root.left)
    print(root.data)
    self.in_order(root.right)

def pre_order(root):
  if root:
    print(root.data)
    self.pre_order(root.left)
    self.pre_order(root.right)

def post_order(root):
  if root:
    self.post_order(root.left)
    self.post_order(root.right)
    print(root.data)


def main():
  pass

if __name__ == "__main__":
  main()