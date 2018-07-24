#Uses python3
import sys
from collections import OrderedDict

class Node:
  def __init__(self, label):
    self.label = label
    self.next = {}

class SuffixTree:
  def __init__(self):
    self.root = Node(None)
  
  def insert(self, text):
    n = len(text)
    for i in range(n - 1, -1, -1):
      current = self.root
      j = i
      while j < n:
        if text[j] in current.next:
          _next = current.next[text[j]]
          label = _next.label
          k = j + 1
          while k - j < len(label) and label[k - j] == text[k]:
            k += 1
          if k - j == len(label):
            current = _next
            j = k
          else:
            exist, new = label[k - j], text[k]
            mid = Node(label[:k - j])
            mid.next[new] = Node(text[k:])
            mid.next[exist] = _next
            _next.label = label[k - j:]
            current.next[text[j]] = mid
        else:
          current.next[text[j]] = Node(text[j:])

def print_output(root):
  for child in root.next:
    print(root.next[child].label)
    print_output(root.next[child])


if __name__ == '__main__':
    text = 'AAC$'
    T = SuffixTree()
    T.insert(text)
    print_output(T.root)

"""
AAC$
$
CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT
AAAAAAAAAAAAAAAAAAAA
TTTTTTTTTTTTTTTTTTTT
CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT
ATGCGATGACCTGACTGA
CTCAACGTATTGGCCAGA
"""