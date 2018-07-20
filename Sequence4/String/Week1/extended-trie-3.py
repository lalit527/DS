#Uses python3
import sys
from collections import OrderedDict

class Node:
  def __init__(self, label, data = None):
    self.data = data
    self.children = [None] * 26
    self.eos = False
    self.label = label
  
  # def __str__(self):
  #   return str(self.data) + str(self.children) + str(self.label)

class Trie:
  def __init__(self):
    self.root = Node(0)
    self.label = 0
  
  def get_index(self, c):
    return ord(c) - ord('A')

  def insert(self, patterns):
    for pattern in patterns:
      self._insert(pattern)

  def _insert(self, text):
    root = self.root
    for c in text:
      i = self.get_index(c)
      # print(c, i, root.data)
      if root.children[i] is None:
        # print(root.label)
        node = Node(self.label + 1, c)
        self.label += 1
        root.children[i] = node
      else:
        pass
      root = root.children[i]
    root.eos = True
  
  def search(self, patterns):
    D = OrderedDict()
    for pattern in patterns:
      self._search(pattern, D)
    for key, value in D.items():
      print(key+ ':' + value)

  def _search(self, pattern, D):
    root = self.root
    prev = None
    for c in pattern:
      i = self.get_index(c)
      prev = root
      root = root.children[i]
      if root is not None:
        D[str(prev.label) + '->' + str(root.label)] = c

def _prefixTrieMatch(text, trie, index, s):
  root = trie.root
  for c in text:
    i = trie.get_index(c)
    if root.children[i] is not None and root.children[i].eos:
      s.append(str(index))
      break
    elif root.children[i] is not None:
      root = root.children[i]
    else:
      return


def prefixTrieMatch(text, trie):
  i = 0
  S = []
  while len(text) > 0:
    _prefixTrieMatch(text, trie, i, S)
    i += 1
    text = text[1:]
  # for key in S:
  #   print(key, end = ' ')
  # print('')
  print(' '.join(S))

if __name__ == '__main__':
    # n = sys.stdin.read()
    # text = sys.stdin.read()
    # print(text)
    # T = Trie()
    # T._insert(text)
    text, n, *patterns = sys.stdin.read().split()
    # print(text)
    T = Trie()
    T.insert(patterns)
    prefixTrieMatch(text, T)
