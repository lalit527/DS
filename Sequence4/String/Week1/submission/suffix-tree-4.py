#Uses python3
import sys
sys.setrecursionlimit(10**7)
from collections import OrderedDict

class Node:
  def __init__(self, label):
    self.label = label
    self.next = {}


class SuffixTree:
  def __init__(self):
    self.root = Node(None)
  
  def insert(self, text):
    for i in range(len(text) - 1, -1, -1):
      current = self.root
      j = i
      while j < len(text):
        if text[j] in current.next:
          child = current.next[text[j]]
          label = child.label
          k = j + 1
          while k - j < len(label) and text[k] == label[k - j]:
            k += 1
          if k - j == len(label):
            current = child
            j = k
          else:
            exist, new = label[k - j], text[k]
            mid = Node(label[:k - j])
            mid.next[new] = Node(text[k:])
            mid.next[exist] = child
            child.label = label[k - j:]
            current.next[text[j]] = mid
        else:
          current.next[text[j]] = Node(text[j:])
    

def print_output(root):
  for child in root.next:
    print(root.next[child].label)
    print_output(root.next[child])


if __name__ == '__main__':
    patterns = sys.stdin.read().split()
    text = ''.join(patterns)
    T = SuffixTree()
    T.insert(text)
    print_output(T.root)