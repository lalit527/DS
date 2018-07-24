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
    
def print_output(root, r):
  for child in root.next:
    result = root.next[child].label
    if result.find("#") > 0:
      print(result)
      r.res += result[0]
    print_output(root.next[child], r)

class Result:
  def __init__(self):
    self.res = ''

if __name__ == '__main__':
    patterns = sys.stdin.read().split()
    text = patterns[0]
    pattern = patterns[1]
    T = SuffixTree()
    T.insert(text + '#' + pattern + '$')
    r = Result()
    print_output(T.root, r)
    print('sssss',r.res)