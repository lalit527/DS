from singlelist import SingleLinkList, Node

def reverseList(T):
  node =  _reverseList(T.head)
  T.head = node

def _reverseList(root):
  if root is None:
    return root
  prev = None
  frwd = root.next
  while root is not None:
    root.next = prev
    prev = root
    root = frwd
    frwd = frwd.next if frwd else None

  return prev

def revrseNnode(T, k):
  node =  _revrseNnode(T.head, k)
  T.head = node

def _revrseNnode(root, k):
  if root is None:
    return root
  n = 1
  prev = None
  frwd = root.next
  while root is not None and n <= k:
    root.next = prev
    prev = root
    root = frwd
    frwd = frwd.next if frwd else None   
    n += 1
  if root is not None and prev.next is not None:
    prev.next.next = _revrseNnode(root, k)
  # print(prev.key if prev else None)
  return prev

def main():
  s = SingleLinkList()
  arr = [1, 2, 3, 4, 5]
  for i in arr:
    s.insert(i)

  print(revrseNnode(s, 2))
  s.printData()

if __name__ == '__main__':
  main()