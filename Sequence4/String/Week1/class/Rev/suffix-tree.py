from collections import OrderedDict

class Node:
  def __init__(self, label, n = 0):
    self.node = n
    self.next = {}
    self.label = label

class Edge:
  def __init__(self, e):
    self.label = e
    self.start = None
    self.end = None

class SuffixTree:
  def __init__(self):
    self.root = Node(0)

  def insert(self, text):
    n = len(text)
    for i in range(n - 1, -1, -1):
      current = self.root
      j = i
      while j < n:
        if text[j] in current.next:
          child = current.next[text[j]]
          label = child.label
          k = j + 1
          m = len(label)
          while k - j < m and text[k] == label[k - j]:
            k += 1
          if k - j == m:
            current = child
            j = k
          else:
            exist, new = label[k - j], text[k]
            mid = Node(label[:k - j])
            mid.next[new] = Node(text[k:], i)
            mid.next[exist] = child
            child.label = label[k - j:]
            current.next[text[j]] = mid
        else:
          current.next[text[j]] = Node(text[j:], i)


def print_output(root):
  for child in root.next:
    print(root.next[child].label)
    print_output(root.next[child])


if __name__ == '__main__':
    text = 'AAC$'
    T = SuffixTree()
    T.insert(text)
    print_output(T.root)